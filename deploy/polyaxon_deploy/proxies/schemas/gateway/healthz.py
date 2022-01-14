#!/usr/bin/python
#
# Copyright 2018-2021 Polyaxon, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from polyaxon_deploy.proxies.schemas.base import get_config

HEALTHZ_LOCATION_OPTIONS = r"""
location /healthz/ {{
    access_log off;
    return 200 "healthy";
}}
"""


def get_healthz_location_config():
    return get_config(
        options=HEALTHZ_LOCATION_OPTIONS,
        indent=0,
    )