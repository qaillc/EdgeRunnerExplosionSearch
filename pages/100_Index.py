import streamlit as st
st.markdown("\n\n\n")


word_text = """
Mathematical Framework for Optimized Base Conversions
 
Introduction:
This document explores base conversions, skipping algorithms, and their applications in different base systems. We discuss algorithms for skipping numbers based on specific criteria and analyze computational efficiency. Additionally, we look at practical applications in tokens and search engines.
 
 
Important Links
 
n  Found Video For Base (50256) : View Here
n  Tokenisor for start up : Website Link
n  Link to Program : Program Link
 
 
Major Discovery
Ø  Math relating the decimal number to the decimal conversion
Ø  The decimal number relate to the converted base decimal number
 
Examples
Ø   Base-2
Sequence : 0 1 10 11 100 101 111
 
Ø   Base-9
Sequence : 0 1 2-9 10 11 12-99 100 101 102-109 110 111
 
Skipping Algorithm
Ø  10 – 2 (skip 8 numbers) = 10 – 2 = 8
Ø   that the conversion is just : decimal – number skipped.
 
 
What we got ?
ü  So, we changed an exponential problem into a subtraction problem
ü  Now in this way we are saving major computational space
ü  What we are doing ? We are saving computational Power
ü  Best optimized way for base conversions
ü  Applied Mathematics to make conversion efficient
 
 
 
Examples
Skipping Algorithm
Definition: A skipping algorithm determines which numbers to exclude based on specific digits or patterns. This is useful for various base systems and applications like tokenization.
Base-2 Example:
In base-2, we skip numbers containing the digit '2'. Sequence: 0, 1, 10, 11, 100, 101, 110, 111.
Base-5 Example:
For base-5, skip numbers containing the digit '5'. Sequence: 0, 1, 2, 3, 4, 10, 11, 12, 13, 14, 20, 21, 22, 23, 24, 30, 31, 32, 33, 34, 40, 41, 42, 43, 44.
Base-9 Example:
Skip numbers with '5'. Sequence: 0, 1, 2, 3, 4, 6, 7, 8, 10, 11, 12, 13, 14, 16, 17, 18, 20, 21, 22, 23, 24, 26, 27, 28, 30, 31, 32, 33, 34, 36, 37, 38, 40, 41, 42, 43, 44, 46, 47, 48, 50, …   
 Code Example
To skip numbers with a specific digit (e.g., 5), you can implement the following Python code:
 def skip_numbers(max_value, skip_digit):
              result = []
              for i in range(max_value + 1):
                  if string(skip_digit) not in string(i):
                      result.append(i)
              return result
 
 
 
Constructs
 
Ø  X-axis 00000-00000-00000-00000-00000
Ø  y-axis 00000-00000-00000-00000-00000
 
Let’s suppose we have a number named W3.
W3-Total number - 00000-00000-00000-00000-00000-00000-00000-00000-00000-00000
 
Major Exponential Calculation For W3
A9x50256^9+ A8x50256^8+ A7x50256^7+ A6x50256^6+ A5x50256^5+ A4x50256^4+ A3x50256^3+ A2x50256^2+A1x50256^1 + A0
 
Optimized Subtraction Calculation
W3 - Numbers Skipped 
 
JS Transformer in Hugging Face
 
https://huggingface.co/docs/transformers.js/en/index
https://huggingface.co/docs/transformers.js/en/api/tokenizers
https://huggingface.co/spaces/eaglelandsonce/JSTokenizer
 
 
 
 
Efficiency
 
Computation Costs for Base Conversion
Base conversion involves changing a number from one base to another. The computational cost includes power calculations, multiplications, and additions.
Example Calculation:
For the polynomial N=A9×502569+A8×502568+⋯+A0N = A_9 \times 50256^9 + A_8 \times 50256^8 + \dots + A_0N=A9 ×502569+A8 ×502568+⋯+A0 :
1. Power Calculations:  10 power calculations (one for each term) O(log⁡B)O(\log B)O(log B) each.
    * Total: 10×O(log⁡B)=O(10log⁡B)10 \times O(\log B) = O(10\log B)10×O(log B)=O(10logB)
2. Multiplications: 10 multiplications O(log⁡B)O(\log B)O(log B) each.
    * Total: 10×O(log⁡B)=O(10log⁡B)10 \times O(\log B) = O(10\log B)10×O(log B)=O(10logB)
3. Additions: 9 additions O(1)O(1)O(1) each.
    * Total: 9×O(1)=O(9)9 \times O(1) = O(9)9×O(1)=O(9)
 
Computation Costs for Simple Subtraction
For the simple subtraction N−1N - 1N−1:
1. Subtraction: 1 subtraction O(1)O(1)O(1).
    * Total: O(1)O(1)O(1)
 
Optimization
 Calculation for B=50256B = 50256B=50256
* log⁡50256≈15.5\log 50256 \approx 15.5log50256≈15.5 (assuming base-2 logarithm)
Time Complexity Breakdown
* Base Conversion:
    * Power Calculations: 10×15.5=15510 \times 15.5 = 15510×15.5=155 units
    * Multiplications: 10×15.5=15510 \times 15.5 = 15510×15.5=155 units
    * Additions: 9×1=99 \times 1 = 99×1=9 units
    * Total Cost: 155+155+9=319155 + 155 + 9 = 319155+155+9=319 units
* Simple Subtraction:
    * Total Cost: 1 unit
 
Efficiency Ratio
The efficiency ratio between the base conversion and simple subtraction is: Efficiency Ratio = 319 units  
Conclusion
ü  The simple subtraction is approximately 319 times more efficient than performing the full base conversion for this example. This ratio highlights how much faster and less computationally intensive a simple subtraction is compared to evaluating a large polynomial in a high base.
ü  For the number represented by the polynomial A9×50256^9+A8×50256^8+⋯+A0A_9 \times 50256^9 + A_8 \times 50256^8 + \dots + A_0A9 ×502569+A8 ×502568+⋯+A0 , the computational costs are as follows:
* Total Cost for Base Conversion: 321.34 units
* Total Cost for Simple Subtraction: 1 unit
Efficiency Ratio
The simple subtraction is approximately 321.34 times more efficient than performing the full base conversion. This highlights a significant computational savings when choosing a simple subtraction over a complex polynomial evaluation. 
"""

st.markdown(word_text)