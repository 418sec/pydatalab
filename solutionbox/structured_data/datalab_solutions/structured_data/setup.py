# Copyright 2017 Google Inc. All Rights Reserved.
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

import setuptools


NAME = 'structured_data_problem'
VERSION = '0.0.1'

if __name__ == '__main__':
  setuptools.setup(
      name=NAME,
      version=VERSION,
      packages=['trainer', 'preprocess', 'predict'],
      author='Google',
      author_email='cloudml-feedback@google.com',
      test_suite='nose.collector',
      tests_require=['nose'])