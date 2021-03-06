# Copyright 2016 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
# in compliance with the License.  You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License
# is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied.  See the License for the specific language governing permissions and limitations under
# the License.

"""Google Cloud Platform library - Monitoring Functionality."""

from __future__ import absolute_import

from google.cloud.monitoring import enums
from ._group import Groups
from ._metric import MetricDescriptors
from ._query import Query
from ._query_metadata import QueryMetadata
from ._resource import ResourceDescriptors

Aligner = enums.Aggregation.Aligner
Reducer = enums.Aggregation.Reducer

__all__ = ['Aligner', 'Reducer', 'Groups', 'MetricDescriptors', 'Query', 'QueryMetadata',
           'ResourceDescriptors']
