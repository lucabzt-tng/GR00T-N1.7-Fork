# SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from gr00t.configs.data.embodiment_configs import register_modality_config
from gr00t.data.embodiment_tags import EmbodimentTag
from gr00t.data.types import (
    ActionConfig,
    ActionFormat,
    ActionRepresentation,
    ActionType,
    ModalityConfig,
)

"""
class Moving_point_memory_evaluation_1sec_mem(Moving_point_memory_evaluation):
    video_keys = ["video._view"]
    state_keys = ["state.axes"]
    action_keys = ["action.pos"]
    language_keys = ["annotation.human.task_description"]
    state_slices = [(0,2)]  
    observation_indices = list(range(-70, 1, 10))  ## -70, -60, -50, -40, -30, -20, -10, 0
"""


movingpoint_base_config = {
    "video": ModalityConfig(
        delta_indices=list(range(-70, 1, 10)),
        modality_keys=["_view"],  # front third-person view + wrist egocentric
    ),
    "state": ModalityConfig(
        delta_indices=[0],
        modality_keys=[
            "axes",  # abs position of the ball
        ],
    ),
    "action": ModalityConfig(
        delta_indices=list(range(0, 40)),  # predict 40 future steps to test rtc
        modality_keys=[
            "pos",
        ],
        action_configs=[
            # RELATIVE = delta from current state (better generalization) ABSOLUTE = target position
            ActionConfig(
                rep=ActionRepresentation.ABSOLUTE,
                type=ActionType.NON_EEF,  # joint-space, not end-effector
                format=ActionFormat.DEFAULT,
            )
        ],
    ),
    # Language: task instruction from annotation field in the dataset
    "language": ModalityConfig(
        delta_indices=[0],
        modality_keys=["annotation.human.task_description"],
    ),
}

register_modality_config(movingpoint_base_config, embodiment_tag=EmbodimentTag.NEW_EMBODIMENT)
