#!/usr/bin/python
"""Simple multi-set partitioning (simple greedy implementation).

https://en.wikipedia.org/wiki/Partition_problem
"""

import argparse
import collections
import logging
import operator
import sys

_BORDER = '-' * 40
_DESCRIPTION = 'Multi-Set Partitioning Example'
_LOG = logging.getLogger()

_DEFAULT_DATA = [84, 46, 8, 58, 10, 65, 74, 79, 56, 120, 43, 0, 62, 25, 0]


def _ParseFlags(argv):
  parser = argparse.ArgumentParser(description=_DESCRIPTION)
  parser.add_argument(
      '--input-file',
      '-i',
      type=str,
      required=False,
      default=None,
      help='Name of input file')
  parser.add_argument(
      '--set-count',
      '-s',
      type=int,
      required=True,
      default=2,
      help='Number of partitioned sets.')
  flags = parser.parse_args(argv)
  logging.basicConfig(
      level=logging.INFO,
      format='%(asctime)s %(levelname)-8s %(message)s',
      datefmt='%Y%m%d %H:%M:%S')
  return flags


def _ReadInputFile(file_name):
  input_data = _DEFAULT_DATA
  if file_name:
    with open(file_name, 'r') as f:
      input_data = [int(v) for v in f.readlines()]
  return input_data


def _CheckInvalidInputData(input_data, set_count):
  input_data_len = len(input_data)
  if set_count > input_data_len:
    _LOG.error('set_count (%d) MUST be < length of input data (%d)!', set_count,
               input_data_len)


class Partitions(object):
  """Contain partition logic."""

  def __init__(self, input_data, set_count):
    # Sort normal, pop from the back.
    self._input_data = sorted(input_data)
    self._set_count = set_count
    self._partitions = collections.defaultdict(list)
    self._sums = collections.Counter()
    self._a = ord('A')

  def DebugData(self):
    _LOG.info(_BORDER)
    _LOG.info(self._input_data)
    _LOG.info(self._set_count)
    _LOG.info(self._partitions)
    _LOG.info(self._sums)

  def _MakeSetName(self, offset):
    return chr(self._a + offset)

  def _AddElement(self, set_name, element):
    self._partitions[set_name].append(element)
    self._sums[set_name] += element

  def _AddToLowest(self, value):
    # Grab the key of the lowest sum.
    set_name = sorted(self._sums.items(), key=operator.itemgetter(1))[0][0]
    self._AddElement(set_name, value)

  def InitializePartitions(self):
    for i in range(self._set_count):
      set_name = self._MakeSetName(i)
      element = self._input_data.pop()
      self._AddElement(set_name, element)

  def AllocateRemaining(self):
    while self._input_data:
      self._AddToLowest(self._input_data.pop())

  def PrintSummary(self):
    _LOG.info(_BORDER)
    _LOG.info('Summary')
    for k in sorted(self._partitions):
      _LOG.info('%s: %s (%d)', k, self._partitions[k], self._sums[k])
    _LOG.info(_BORDER)


def main(argv):
  flags = _ParseFlags(argv)

  input_data = _ReadInputFile(flags.input_file)

  _LOG.info(_BORDER)
  _LOG.info('Partitioning %s into %d sets.', input_data, flags.set_count)

  _CheckInvalidInputData(input_data, flags.set_count)

  p = Partitions(input_data, flags.set_count)
  p.InitializePartitions()
  p.AllocateRemaining()
  p.PrintSummary()


if __name__ == '__main__':
  main(sys.argv[1:])
