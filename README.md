### Produces a sorting sequence csv file 

The program uses in the _LAYOUT.xlsx as input - a representation of storage bin layout in the warehouse.
The column header contains the details regarding the sorting sequence, number of pickfaces, reserve locations and warehouse number.

**Example:**    
LaneSingle.1.6.9000
- LaneSingle - Ascending sorting for a single lane    
- 1 - number of 0101 bins    
- 6 - number of 0102 bins    
- 9000 - warehouse number

AisleReverseZig.2.5.7000
- AisleReverseZig - Descending sorting for an Aisle(double lane) in a zig-zag pattern    
- 2 - number of 0101 bins    
- 5 - number of 0102 bins    
- 7000 - warehouse number    
