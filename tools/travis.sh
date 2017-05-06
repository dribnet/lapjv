#!/usr/bin/env bash
set -ex

section test
nosetests $TEST_ARGS lapjv1
section_end test
