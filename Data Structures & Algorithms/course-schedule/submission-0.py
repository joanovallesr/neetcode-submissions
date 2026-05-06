class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = defaultdict(list)
        for c, p in prerequisites:
            prereq[c].append(p)

        def cycle(course, seen):
            if course in seen:
                return True
            
            seen.add(course)
            for p in prereq[course]:
                if cycle(p, seen):
                    return True
            
            prereq[course] = []
            seen.remove(course)
            return False
        
        seen = set()
        for c in range(numCourses):
            if cycle(c, seen):
                return False

        return True