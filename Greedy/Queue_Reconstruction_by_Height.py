class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        reconstructQueue = []
        resort_people = []

        for person in people:
            i = 0
            insert_item = person
            while i < len(resort_people) and insert_item:
                if resort_people[i][0] <  insert_item[0]:
                    resort_people.insert(i, insert_item)
                    insert_item = None
                
                elif resort_people[i][0] == insert_item[0]:
                    if resort_people[i][1] > insert_item[1]:
                        resort_people.insert(i, insert_item)
                        insert_item = None
                
                i += 1
            if insert_item:
                resort_people.append(insert_item)

        for item in resort_people:
            i = 0
            bigger_count = 0
            acc = item
            
            while i < len(reconstructQueue) and acc:
                if reconstructQueue[i][0] >= acc[0]:
                    bigger_count += 1
                
                if bigger_count > acc[1]:
                    reconstructQueue.insert(i, acc)
                    acc = None

                elif bigger_count == acc[1]:
                    reconstructQueue.insert(i + 1, acc)
                    acc = None
                i += 1
            
            if acc:
                reconstructQueue.append(acc)
        
        
        return reconstructQueue


assert Solution().reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]) == [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]