# Copyright 2018 Xanadu Quantum Technologies Inc.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Core expectations
=================

OpenQML also supports a collection of built-in quantum **expectations**,
including both discrete-variable (DV) expectations as used in the qubit model,
and continuous-variable expectations as used in the qumode model of quantum
computation.

Here, we summaries the built-in expectations supported by OpenQML, as well
as the conventions chosen for their implementation.

.. note::

    If writing a plugin device for OpenQML, make sure that your plugin
    supports the required OpenQML built-in expectations defined here,
    by including them in your device ``_observable_map``.

    If the operator convention differs between the built-in OpenQML operator
    and the corresponding expectation in the targeted framework, ensure that the
    conversion between the two conventions takes places automatically
    by the plugin device.


.. rst-class:: contents local topic

.. toctree::
   :maxdepth: 2

   expectation/discrete
   expectation/continuous
"""

from .builtins_continuous import *
from .builtins_discrete import *
