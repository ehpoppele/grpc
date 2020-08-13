# Copyright 2015 gRPC authors.
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
"""Common resources used in the gRPC route guide example."""

import json

import grpc

protos = grpc.protos("route_guide.proto")


def read_route_guide_database():
    """Reads the route guide database.

  Returns:
    The full contents of the route guide database as a sequence of
      protos.Features.
  """
    feature_list = []
    with open("route_guide_db.json") as route_guide_db_file:
        for item in json.load(route_guide_db_file):
            feature = protos.Feature(
                name=item["name"],
                location=protos.Point(latitude=item["location"]["latitude"],
                                      longitude=item["location"]["longitude"]))
            feature_list.append(feature)
    return feature_list
