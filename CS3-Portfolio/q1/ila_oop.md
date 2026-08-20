=============================================================================
                  SARI-SARI STORE INVENTORY SYSTEM (OOP)
=============================================================================

                   ⌁————————————————————————————————⌁
                   |         Sari-Sari Store        |
                   +--------------------------------+
                   | - inventory: List<Item>        |
                   +--------------------------------+
                   | + add_item(item)               |
                   | + display_inventory_value()    |
                   ⌁————————————————————————————————⌁
                                   |
                                   |  [ABSTRACTION]
                                   |  (Store owner uses simple actions,
                                   v   hiding internal math/loops)
                   ⌁————————————————————————————————⌁
                   |             Item               |  <-- [ENCAPSULATION]
                   +--------------------------------+      (Bundles name, price,
                   | - name: String                 |       qty; hides variables
                   | - price: Float                 |       behind private state)
                   | - quantity: Int                |
                   +--------------------------------+
                   | + get_name()                   |
                   | + calculate_total()*           |
                   ⌁————————————————————————————————⌁
                                   ^
                                   |
            +----------------------+----------------------ᓚᘏᗢ
            |                      |                      |
    [INHERITANCE]          [INHERITANCE]          [INHERITANCE]
            |                      |                      |
            v                      v                      v
+-----------------------+ +-----------------------+ +-----------------------+
|     StandardItem      | |    PerishableItem     | |      PromoItem        |
+-----------------------+ +-----------------------+ +-----------------------+
|                       | | - days_left: Int      | | - discount_rate: Float|
+-----------------------+ +-----------------------+ +-----------------------+
| + calculate_total()   | | + calculate_total()   | | + calculate_total()   |
+-----------------------+ +-----------------------+ +-----------------------+
            |                      |                      |
            +----------------------+----------------------+
                                   |
                                   v
                            [POLYMORPHISM]
              (Each item type calculates total differently:
               Standard  --> Price * Quantity
               Perishable--> 50% discount if expiring
               Promo     --> Applies promo discount %)
=============================================================================

### 1. Encapsulation
## Encapsulation refers to bundling data and methods into one unit and restricting access to internal state – it is essentially data hiding. This applies to the Sari-Sari Store Inventory System by collecting the 15 separate variables into a single Item class. 

### 2. Abstraction
## Abstraction means hiding complex implementation details and showing only what is necessary to the outside user. In the problem, the store owner only interacts with simple operations to avoid confusion. 

### 3. Inheritance
## Inheritance is somewhat self-explanatory. It allows a new class to adopt attributes from an existing class to reuse code. The developer can make a fundamental Item class with the variables, then specialized “child” classes for organization. 

### 4. Polymorphism
## Polymorphism is seen as allowing different classes to respond to the same action in their own ways. Different item types can calculate their final sale price differently using the exact same method call; for example, “calculate_total()” 

## Reflection
## Among the four pillars in OOP,  encapsulation would be most useful for the system. Encapsulation is essentially the “organization” pillar of OOP. This would be best suited for the sari-sari store’s inventory management. It deals with managing the items; additionally, it can only be accessed by the developer (sari-sari store owner) and not the outside users (buyers).


