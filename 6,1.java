public int repeatedNumber(final List<Integer> list)
{
  if (list.size() <= 1)
  {
    return -1;
  }

  Collections.sort(list);

  for (int i = 0; i < list.size() - 1; i++)
  {
    if (list.get(i) == list.get(i + 1))
    {
      return list.get(i);
    }
  }

  return -1;
}