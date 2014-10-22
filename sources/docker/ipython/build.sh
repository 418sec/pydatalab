#!/bin/sh
# Copyright 2014 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Builds the IPython docker image

# Create a versioned Dockerfile based on current date
VERSION=`date +%Y%m%d`
SUBSTITUTION="s/_version_/v$VERSION/"
cat Dockerfile.in | sed $SUBSTITUTION > Dockerfile

# Copy build outputs as a dependency of the Dockerfile
cp -R ../../../build build

# Build the docker image
docker build -t gcp-ipython .

# Finally cleanup
rm -rf build
rm Dockerfile

