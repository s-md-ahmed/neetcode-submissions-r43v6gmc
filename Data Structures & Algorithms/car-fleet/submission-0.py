class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time=[]
        mymap={}
        for i in range(len(position)):
            mymap[position[i]]=speed[i]
        
        # Create a clean, empty dict to hold the sorted version
        sorted_map = {}

        # Sort the keys and build the new map step-by-step
        for k in sorted(mymap.keys(), reverse=True):
            sorted_map[k] = mymap[k]
        # Assuming sortedmap is already built and sorted by key
        for k in sorted_map:
            # k is the position, sortedmap[k] is the speed
            t = (target - k) / sorted_map[k]
            time.append(t)
        stack=[]
        stack.append(time[0])
        for i in range(1,len(position)):
            while stack and time[i]>stack[-1]:
                stack.append(time[i])
            
        print(stack)

        
        return len(stack)
        