from collections import deque
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        prereqs_of_class = {course: set() for course in range(numCourses)}
        classes_after = {course: set() for course in range(numCourses)}
        
        # convert into prereqs_of_class_list {clas : set of prereqs}
        for req in prerequisites:
            prereqs_of_class[req[0]].add(req[1])
            classes_after[req[1]].add(req[0])

        # populate queue initially
        q = deque()
        for clas in prereqs_of_class:
            if len(prereqs_of_class[clas]) == 0:
                q.append(clas)

        # topological sort
        taken_count = 0
        while q:
            taken = q.pop()
            taken_count +=1
            for candidate in classes_after[taken]:
                prereqs_of_class[candidate].remove(taken)

                if len(prereqs_of_class[candidate]) == 0:
                    q.append(candidate)
        
        return len(q) == 0 and taken_count >= numCourses
        