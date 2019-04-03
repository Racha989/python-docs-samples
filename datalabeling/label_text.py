#!/usr/bin/env python

# Copyright 2019 Google LLC
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

import argparse


# [START datalabeling_label_text_beta]
def label_text(dataset_resource_name, instruction_resource_name,
                             annotation_spec_set_resource_name):
    """Labels a text dataset."""
    from google.cloud import datalabeling_v1beta1 as datalabeling
    client = datalabeling.DataLabelingServiceClient()

    basic_config = datalabeling.types.HumanAnnotationConfig(
            instruction=instruction_resource_name,
            annotated_dataset_display_name='YOUR_ANNOTATED_DATASET_DISPLAY_NAME',
            label_group='YOUR_LABEL_GROUP',
            replica_count=1)

    feature = datalabeling.enums.LabelTextRequest.Feature.TEXT_ENTITY_EXTRACTION

    text_entity_extraction_config = datalabeling.types.TextEntityExtractionConfig(
            annotation_spec_set=annotation_spec_set_resource_name)

    response = client.label_text(
            dataset_resource_name,
            basic_config,
            feature,
            text_entity_extraction_config=text_entity_extraction_config)

    print('Label_text operation name: {}'.format(response.operation.name))
    return response
# [END datalabeling_label_text_beta]

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
            description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument(
            '--dataset-resource-name',
            help='Dataset resource name. Required.',
            required=True)

    parser.add_argument(
            '--instruction-resource-name',
            help='Instruction resource name. Required.',
            required=True)

    parser.add_argument(
            '--annotation-spec-set-resource-name',
            help='Annotation spec set resource name. Required.',
            required=True)

    args = parser.parse_args()

    label_text(args.dataset_resource_name, args.instruction_resource_name,
                         args.annotation_spec_set_resource_name)
