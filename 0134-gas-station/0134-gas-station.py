class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = 0
        total_cost = 0
        current_gas = 0
        starting_station = 0
        
        for i in range(len(gas)):
            total_gas += gas[i]
            total_cost += cost[i]
            current_gas += gas[i] - cost[i]
            
      
            if current_gas < 0:
                starting_station = i + 1
                current_gas = 0
        
     
        if total_gas < total_cost:
            return -1
        else:
            return starting_station


