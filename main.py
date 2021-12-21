
def count_batteries_by_usage(cycles):
    counts={'lowCount':0,'mediumCount':0,'highCount':0}
    for cycle in cycles:
        if cycle<150:
            counts['lowCount']+=1
        elif cycle>=150 and cycle<650:
            counts['mediumCount']+=1
        else:
            counts['highCount']+=1
    return {
        'lowCount':counts['lowCount'],
        'mediumCount':counts['mediumCount'],
        'highCount':counts['highCount']
    }

def test_bucketing_by_number_of_cycles():
  print("Counting batteries by usage cycles...\n");
  counts = count_batteries_by_usage([100, 300, 500, 600, 900, 1000])
  assert(counts["lowCount"] == 1)
  assert(counts["mediumCount"] == 3)
  assert(counts["highCount"] == 2)
  print(counts)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_number_of_cycles()
