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