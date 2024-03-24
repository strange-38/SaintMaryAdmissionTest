import numpy as np

def calculate_growth_rate(GDP: list) -> list:
    """
    Calculate the growth rate for each year based on GDP values.

    Parameters:
    GDP (list of float): List of GDP values for consecutive years.

    Returns:
    list of float: List of growth rates for consecutive years.
    """
    GR = []
    for i in range(len(GDP)-1):
        current_year = GDP[i+1]
        previous_year = GDP[i]
        grwth_rate = (current_year - previous_year) / previous_year * 100
        GR.append(grwth_rate)
    return GR

def calculate_ranking(GR: list) -> list:
    """
    Assign a ranking based on growth rates.

    Parameters:
    GR: List of growth rates for consecutive years.

    Returns:
    ranking: List of rankings corresponding to growth rates.
    """
    ranking = []
    for rate in GR:
        if rate > 25:
            ranking.append("Exceptional")
        elif rate > 0:
            ranking.append("Good")
        else:
            ranking.append("Poor")
    return ranking

def calculate_AAGR(GR: list) -> float:
    """
    Calculate the Average Annual Growth Rate (AAGR) from a list of growth rates.

    Parameters:
    GR: List of growth rates for consecutive years.

    Returns:
    float: Average Annual Growth Rate (AAGR).
    """
    return round(np.mean(GR), 2)

def calculate_CAGR(GDP: list) -> float:
    """
    Calculate the Compound Annual Growth Rate (CAGR) from a list of GDP values.

    Parameters:
    GDP: List of GDP values for consecutive years.

    Returns:
    float: Compound Annual Growth Rate (CAGR).
    """
    ending_year = GDP[-1]
    beginning_year = GDP[0]
    n = len(GDP)-1 # Number of years
    return round(((ending_year/beginning_year)**(1/n) - 1) * 100, 2)

def calculate_stdev(GR: list) -> float:
    """
    Calculate the standard deviation of growth rates.

    Parameters:
    GR: List of growth rates for consecutive years.

    Returns:
    float: Sample Standard deviation of growth rates.
    """
    return round(np.std(GR, ddof = 1), 3)

def main():
    """
    Main function to gather information about countries and analyze their economic data.
    """

    a = int(input("Enter the number of countries: "))
    n = int(input("Enter the number of years: "))

    countries = []
    for i in range(a):
        country_name = input(f"\nEnter the name of country {i+1}: ")
        print(f"\nCountry {country_name}")
        print("-"*60)
        GDP_begin = float(input("Enter the beginning GDP value: "))
        GDP_values = [float(input(f"Enter the end of year {j+1} GDP value: ")) for j in range(n)]
        GDPB_values = [GDP_begin]+GDP_values
        GR_values = calculate_growth_rate(GDPB_values)
        ranking = calculate_ranking(GR_values)
        average_annual_growth_rate = calculate_AAGR(GR_values)
        compund_annual_growth_rate = calculate_CAGR(GDPB_values)
        stdev = calculate_stdev(GR_values)
        countries.append({
            "name": country_name,
            "GDP": GDP_values,
            "GR": GR_values,
            "ranking": ranking,
            "AAGR": average_annual_growth_rate,
            "CAGR": compund_annual_growth_rate,
            "stdev": stdev
        })

    min_stdev_country = min(countries, key=lambda x: x["stdev"])

    for country in countries:
        # print header
        print("\n", country['name'].center(70))
        print("-"*70)
        print("{:<15s} {:<18s} {:<20s} {:<16s}".format("Year", "GDP Value", "Growth Rate", "Ranking"))
        print("-"*70)
        
        for year in range(len(country["GDP"])):
            print("{:<15d} ${:<18,.2f} {:.2f} {:<15s} {:<16s}".format(year+1, country['GDP'][year], country['GR'][year], "%", country['ranking'][year]))
            
        print(f"Average Annual Growth Rate: {country['AAGR']:.2f}%")
        print(f"Compound Annual Growth Rate: {country['CAGR']:.2f}%")
        print(f"Standard Deviation: {country['stdev']:.3f}")

    if min_stdev_country["stdev"] < 25:
        print(f"\nThe Country {min_stdev_country['name']}'s economy is most stable.")
    else:
        print(f"\nThe Country {min_stdev_country['name']}'s economy is least risky.")

if __name__ == "__main__":
    main()
