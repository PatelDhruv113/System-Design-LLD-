# L - Liskov Substitution Principle (LSP)

## Definition
The **Liskov Substitution Principle (LSP)** states that **objects of a child class should be replaceable with objects of the parent class without breaking the correctness of the program**.

In simple words, if a class inherits from another class, the child class should behave in a way that does not violate the expectations of the parent class.

---

## Simple Explanation

- A **Child class** should behave like its **Parent class**.
- You should be able to replace a **Parent object** with a **Child object** without changing the program's behavior.
- The Child class should **not break the contract or behavior** promised by the Parent class.
