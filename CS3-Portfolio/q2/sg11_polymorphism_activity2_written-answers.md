# 1. Answer the following questions:
## a. What is duck typing, as explained in the video?
### - Duck typing is an alternative way to achieve polymorphism in Python. It doesn't rely on class inheritance; meaning, an object can be treated as a specific type as long as it possess the minimum necessary attributes and methods required of that type. Duck typing follows the adage: "If it looks like a duck and quacks like a duck, it must be a duck."
## b. What did the Car class need to have so it could work inside the same loop as Dog and Cat, even if it does not inherit from the Animal class?
### - In order to work inside the same loop without inheriting from Animal, the Car class needed to satisfy the same minimum requirements: a speak method to successfully respond to the loop calling, and the alive attribute so it wouldn't raise an AttributeError when the loop tried to access the property. 

# 3. How does the code in 2.2 demonstrate polymorphism?
### - yes yes
