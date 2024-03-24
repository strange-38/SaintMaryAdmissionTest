import math

def calculate_square_pyramid_properties(h:int, a: int) -> tuple:
    """
    Calculate the volume, Lateral Surface Area (LSA), Total Surface Area (TSA), and slant height of a square pyramid.

    Parameters:
        h (int): Height of the square pyramid.
        a (float): Side length of the square pyramid.

    Returns:
        tuple: A tuple containing the calculated volume, LSA, TSA, and slant height.
    """
    volume = (1/3) * (a ** 2) * h

    slant_height = math.sqrt((a / 2) ** 2 + h ** 2)
    
    LSA = 2 * a * slant_height
    
    TSA = LSA + (a ** 2)
    
    return round(volume), round(LSA, 3), round(TSA, 3), round(slant_height, 3)

def main():
    """
    Main function to calculate and display the properties of a square pyramid.
    """
    print("\nThe program prints the volume, LSA, TSA and slant height of a square pyramid\nhaving height h being an odd number ranging from 1 to N and side length a.")
    # Taking input from the user
    N = int(input("Enter the number for maximum height (N): "))
    a = float(input("Enter the side length (a) of the square pyramid: "))

    # Print header
    print("{:<10s} {:<10s} {:<24s} {:<22s} {:<15s}".format("Height", "Volume", "Lateral Surface Area", "Total Surface Area", "Slant Height"))
    print("-" * 83)

    for h in range(1, N+1):
        # Execute for odd number only
        if h%2 != 0:
            volume, LSA, TSA, slant_height = calculate_square_pyramid_properties(h, a)
            print("{:<10d} {:d} m\u00B3 {:<10s} {:.3f} m\u00B2 {:<10s} {:.3f} m\u00B2 {:<10s} {:.3f} m".format(h, volume, "", LSA, "", TSA, "", slant_height))

if __name__ == "__main__":
    main()

