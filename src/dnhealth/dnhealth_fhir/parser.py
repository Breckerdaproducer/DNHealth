# Copyright 2025 DNAi inc.

# Dual-licensed under the DNAi Free License v1.1 and the
# DNAi Commercial License v1.1.
# See the LICENSE files in the project root for details.

"""Compatibility parser exports for FHIR resources."""

from dnhealth.dnhealth_fhir.parser_json import parse_fhir_json, parse_resource
from dnhealth.dnhealth_fhir.parser_xml import parse_fhir_xml

__all__ = ["parse_fhir_json", "parse_fhir_xml", "parse_resource"]
