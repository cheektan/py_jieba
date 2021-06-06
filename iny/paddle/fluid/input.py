#   Copyright (c) 2019 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import print_function
import warnings
from .framework import Variable, in_dygraph_mode, static_only
from .layer_helper import LayerHelper
from .data_feeder import check_variable_and_dtype, check_dtype
from ..utils import deprecated

__all__ = ['one_hot', 'embedding']


@deprecated(since='2.0.0', update_to='paddle.nn.functional.one_hot')
def one_hot(input, depth, allow_out_of_range=False):
    """
    :alias_main: paddle.nn.functional.one_hot
	:alias: paddle.nn.functional.one_hot,paddle.nn.functional.common.one_hot
	:old_api: paddle.fluid.one_hot

    The operator converts each id in the input to an one-hot vector with a
    depth length. The value in the vector dimension corresponding to the id
    is 1, and the value in the remaining dimension is 0.

    The shape of output Tensor or LoDTensor is generated by appending depth dimension
    behind the last dimension of the input shape.

    .. code-block:: text

        Example 1 (allow_out_of_range=False):

        input:
            X.shape = [4]
            X.data = [1, 1, 3, 0]
            depth = 4

        output:
            Out.shape = [4, 4]
            Out.data = [[0., 1., 0., 0.],
                        [0., 1., 0., 0.],
                        [0., 0., 0., 1.],
                        [1., 0., 0., 0.]]

        Example 2 (allow_out_of_range=True):

        input:
            X.shape = [4]
            X.data = [1, 1, 5, 0]
            depth = 4
            allow_out_of_range = True

        output:
            Out.shape = [4, 4]
            Out.data = [[0., 1., 0., 0.],
                        [0., 1., 0., 0.], 
                        [0., 0., 0., 0.], # This id is 5, which goes beyond depth, so set it all-zeros data.
                        [1., 0., 0., 0.]]

        Example 3 (allow_out_of_range=False):

        input:
            X.shape = [4]
            X.data = [1, 1, 5, 0]
            depth = 4
            allow_out_of_range = False

        output: Throw an exception for Illegal value
            The second dimension in X is 5, which is greater than depth.  
            Allow_out_of_range =False means that does not allow the word id to exceed depth,
            so it throws an exception.


    Args:
        input(Variable): Tensor or LoDTensor with shape :math:`[N_1, N_2, ..., N_k]` ,
            which contains at least one dimension. The data type is int32 or int64.
        depth(int): An integer defining the depth of the one hot dimension. If input 
            is word id, depth is generally the dictionary size.
        allow_out_of_range(bool): A bool value indicating whether the input
            indices could be out of range :math:`[0, depth)` . When input indices are
            out of range, exceptions :code:`Illegal value` is raised if :attr:`allow_out_of_range`
            is False, or zero-filling representations is created if it is set True.
            Default: False.

    Returns:
        Variable: The one-hot representations of input. A Tensor or LoDTensor with type float32.

    Examples:
        .. code-block:: python

            import paddle.fluid as fluid
            # Correspond to the first example above, where label.shape is 4 and one_hot_label.shape is [4, 4].
            label = fluid.data(name="label", shape=[4], dtype="int64")
            one_hot_label = fluid.one_hot(input=label, depth=4)
    """
    check_variable_and_dtype(input, 'input', ['int32', 'int64'], 'one_hot_v2')
    helper = LayerHelper("one_hot_v2", **locals())

    one_hot_out = helper.create_variable_for_type_inference(dtype='float32')

    if in_dygraph_mode():
        inputs = {'X': input}
        attrs = {'depth': depth, 'allow_out_of_range': allow_out_of_range}
    else:
        if not isinstance(depth, Variable):
            # user attribute 
            inputs = {'X': input}
            attrs = {'depth': depth, 'allow_out_of_range': allow_out_of_range}
        else:
            depth.stop_gradient = True
            inputs = {'X': input, 'depth_tensor': depth}
            attrs = {'allow_out_of_range': allow_out_of_range}
    helper.append_op(
        type="one_hot_v2",
        inputs=inputs,
        attrs=attrs,
        outputs={'Out': one_hot_out},
        stop_gradient=True)
    return one_hot_out


@static_only
@deprecated(since='2.0.0', update_to='paddle.nn.functional.embedding')
def embedding(input,
              size,
              is_sparse=False,
              is_distributed=False,
              padding_idx=None,
              param_attr=None,
              dtype='float32'):
    r"""
    :api_attr: Static Graph

    The operator is used to lookup embeddings vector of ids provided by :attr:`input` . 
    It automatically constructs a 2D embedding matrix based on the
    input :attr:`size` (vocab_size, emb_size) and :attr:`dtype` .

    The shape of output Tensor is generated by appending an emb_size dimension to the
    last dimension of the input Tensor shape.

    **Note:** The id in :attr:`input` must satisfy :math:`0 =< id < size[0]` , 
    otherwise the program will throw an exception and exit.

    .. code-block:: text

        Case 1:

        input is a Tensor. padding_idx = -1
            input.data = [[1, 3], [2, 4], [4, 127]]
            input.shape = [3, 2]
        Given size = [128, 16]
        output is a Tensor:
            out.shape = [3, 2, 16]
            out.data = [[[0.129435295, 0.244512452, ..., 0.436322452],
                        [0.345421456, 0.524563927, ..., 0.144534654]],

                        [[0.345249859, 0.124939536, ..., 0.194353745],
                        [0.945345345, 0.435394634, ..., 0.435345365]],
                        
                        [[0.945345345, 0.435394634, ..., 0.435345365],
                        [0.0,         0.0,         ..., 0.0        ]]]  # padding data
        The input padding_idx is less than 0, it is automatically converted to padding_idx = -1 + 128 = 127
        It will pad all-zero data when ids is 127.
        
        Case 2:

        input is a LoDTensor with 1-level LoD. padding_idx = 0
            input.lod = [[2, 3]]
            input.data = [[1], [3], [2], [4], [0]]
            input.shape = [5, 1]
        Given size = [128, 16]
        output is a LoDTensor:
            out.lod = [[2, 3]]
            out.shape = [5, 1, 16]
            out.data = [[[0.129435295, 0.244512452, ..., 0.436322452]],
                        [[0.345421456, 0.524563927, ..., 0.144534654]],
                        [[0.345249859, 0.124939536, ..., 0.194353745]],
                        [[0.945345345, 0.435394634, ..., 0.435345365]],
                        [[0.0,         0.0,         ..., 0.0        ]]]  # padding data
        It will pad all-zero data when ids is 0.


    Args:
        input(Variable): A Tensor or LoDTensor with type int64, which contains the id information.
            The value of the input id should satisfy :math:`0<= id < size[0]` .
        size(tuple|list): The shape of lookup table parameter. It should have two elements which
            indicates the size of the dictionary of embeddings and the size of each embedding vector respectively.
        is_sparse(bool): The flag indicating whether to use sparse update. This parameter only
            affects the performance of the backwards gradient update. It is recommended to set 
            True because sparse update is faster. But some optimizer does not support sparse update
            In these case, is_sparse must be False. Default: False.
        is_distributed(bool): Whether to store the embedding matrix in a distributed manner. Only used
            in multi-machine distributed CPU training. Default: False.
        padding_idx(int|long|None): padding_idx needs to be in the interval [-vocab_size, vocab_size). 
            If :math:`padding\_idx < 0`, the :math:`padding\_idx` will automatically be converted
            to :math:`vocab\_size + padding\_idx` . It will output all-zero padding data whenever lookup
            encounters :math:`padding\_idx` in id. And the padding data will not be updated while training.
            If set None, it makes no effect to output. Default: None.
        param_attr(ParamAttr): To specify the weight parameter property. Default: None, which means the
            default weight parameter property is used. In addition,
            user-defined or pre-trained word vectors can be loaded with the :attr:`param_attr` parameter. 
            The local word vector needs to be transformed into numpy format, and the shape of local word
            vector should be consistent with :attr:`size` .
        dtype(str|core.VarDesc.VarType): It refers to the data type of output Tensor.
            It must be float32 or float64. Default: float32.

    Returns:
        Variable: Embedding Tensor or LoDTensor mapped by input. The data type is the same as :attr:`dtype` .

    Static Examples:
        .. code-block:: python

            import paddle
            import numpy as np
            paddle.enable_static()
            
            x = paddle.static.data(name="x", shape = [2, 4], dtype=np.int64)
            embedding = paddle.nn.Embedding(10, 3,
                        weight_attr=paddle.nn.initializer.Constant(value=1.0))
            adam = paddle.optimizer.SGD(parameters=[embedding.weight], learning_rate=0.01)
            output = embedding(x)
            m_output=paddle.mean(output)
            
            adam.minimize(m_output)
            
            place = paddle.CPUPlace()
            exe = paddle.static.Executor(place)
            exe.run(paddle.static.default_startup_program())
            
            x = np.array([[7, 2, 4, 5],[4, 3, 2, 9]], dtype=np.int64)
            
            # x is a Numpy.
            # x.data = [[7, 2, 4, 5], [4, 3, 2, 9]]
            # x.shape = [2, 4]
            
            out, = exe.run(paddle.static.default_main_program(), feed={'x':x}, fetch_list=[output])
            
            # out is a Numpy.
            # out.data = [[1., 1., 1.],
            #             [1., 1., 1.],
            #             [1., 1., 1.],
            #             [1., 1., 1.]],
            #
            #            [[1., 1., 1.],
            #             [1., 1., 1.],
            #             [1., 1., 1.],
            #             [0., 0., 0.]]]
            # out.shape = [2, 4, 3]


    Dygraph Examples:
        .. code-block:: python

            import paddle
            import numpy as np

            x_data = np.arange(3, 6).reshape((3, 1)).astype(np.int64)
            
            # x is a Tensor.
            # x.data = [[3], [4], [5]]
            # x.shape = [3, 1]
            x = paddle.to_tensor(x_data, stop_gradient=False)
            
            # embedding weight shape = [10, 3]
            embedding = paddle.nn.Embedding(10, 3, sparse=True)
            
            # embedding weight data = [10, 3]
            w0 = np.full(shape=(10, 3), fill_value=2).astype(np.float32)
            
            # embedding.weight.shape = [10, 3]
            # embedding.weight.data =
            #                        [[2., 2., 2.],
            #                         [2., 2., 2.],
            #                         [2., 2., 2.],
            #                         [2., 2., 2.],
            #                         [2., 2., 2.],
            #                         [2., 2., 2.],
            #                         [2., 2., 2.],
            #                         [2., 2., 2.],
            #                         [2., 2., 2.],
            #                         [2., 2., 2.]]
            embedding.weight.set_value(w0)
            
            adam = paddle.optimizer.Adam(
                parameters=[embedding.weight], learning_rate=0.01)
            adam.clear_grad()
            
            # out is Tensor
            # out.shape: [3, 1, 3]
            # out.layout: NCHW
            # out.dtype: float
            # out.data: [2 2 2 2 2 2 2 2 2]
            out = embedding(x)
            
            out.backward()
            adam.step()

    """

    helper = LayerHelper('embedding', **locals())
    check_variable_and_dtype(input, 'input', ['int64'], 'fluid.embedding')
    check_dtype(dtype, 'dtype', ['float16', 'float32', 'float64'],
                'fluid.embedding')
    remote_prefetch = is_sparse and (not is_distributed)
    if remote_prefetch:
        assert is_sparse is True and is_distributed is False
    w = helper.create_parameter(
        attr=helper.param_attr, shape=size, dtype=dtype, is_bias=False)
    tmp = helper.create_variable_for_type_inference(dtype)
    padding_idx = -1 if padding_idx is None else padding_idx if padding_idx >= 0 else (
        size[0] + padding_idx)
    helper.append_op(
        type='lookup_table_v2',
        inputs={'Ids': input,
                'W': w},
        outputs={'Out': tmp},
        attrs={
            'is_sparse': is_sparse,
            'is_distributed': is_distributed,
            'remote_prefetch': remote_prefetch,
            'padding_idx': padding_idx
        })
    return tmp
