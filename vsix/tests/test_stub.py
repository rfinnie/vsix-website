# SPDX-PackageSummary: vsix-website
# SPDX-FileCopyrightText: Copyright (C) 2020-2025 Ryan Finnie
# SPDX-License-Identifier: MPL-2.0

import unittest
import warnings


class TestStub(unittest.TestCase):
    def test_stub(self):
        # pytest doesn't like a tests/ with no tests
        warnings.warn("Remove this file once unit tests are added")
