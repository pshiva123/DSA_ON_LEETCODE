from collections import defaultdict
import bisect
from typing import List

class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        # 1) Group building coordinates by row and by column
        rows = defaultdict(list)   # rows[x] = sorted list of y’s in row x
        cols = defaultdict(list)   # cols[y] = sorted list of x’s in col y
        for x, y in buildings:
            rows[x].append(y)
            cols[y].append(x)
        
        # 2) Sort each list so we can binary-search
        for x in rows:
            rows[x].sort()
        for y in cols:
            cols[y].sort()
        
        cnt = 0
        # 3) For each building, check if there's at least one neighbor
        #    in each of the 4 directions by binary-searching its row/col lists.
        for x, y in buildings:
            y_list = rows[x]
            i = bisect.bisect_left(y_list, y)
            has_west  = (i > 0)                  # something < y in this row
            has_east  = (i < len(y_list)-1)     # something > y in this row

            x_list = cols[y]
            j = bisect.bisect_left(x_list, x)
            has_south = (j > 0)                  # something < x in this column
            has_north = (j < len(x_list)-1)     # something > x in this column

            if has_west and has_east and has_south and has_north:
                cnt += 1

        return cnt

