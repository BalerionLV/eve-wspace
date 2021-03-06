#   Eve W-Space
#   Copyright 2014 Andrew Austin and contributors
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
from core.models import ConfigEntry
#defaults = [("TEST_SETTING", "BOB")]
defaults = [
        ("MAP_PVP_THRESHOLD", "0"),
        ("MAP_NPC_THRESHOLD", "10"),
        ("MAP_SCAN_WARNING", "3"),
        ("MAP_INTEREST_TIME", "15"),
        ("MAP_ESCALATION_BURN", "3"),
        ]

def load_defaults():
    for setting in defaults:
        config = ConfigEntry.objects.get_or_create(name=setting[0], user=None)[0]
        config.value = setting[1]
        config.save()
