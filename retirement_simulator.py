def calculate_retirement(current_age, retirement_age, current_savings, monthly_contribution, annual_return_rate):
    """
    Calculates the future value of savings at retirement.
    Assumes monthly compounding.
    """
    months_to_retirement = (retirement_age - current_age) * 12
    monthly_return_rate = annual_return_rate / 100 / 12
    
    total_savings = current_savings
    total_contributions = current_savings
    
    for _ in range(months_to_retirement):
        # Calculate interest for the current month
        interest = total_savings * monthly_return_rate
        # Add interest and monthly contribution to the total
        total_savings += interest + monthly_contribution
        # Track the total principal contributed
        total_contributions += monthly_contribution
        
    return total_savings, total_contributions

def main():
    print("=== Basic Retirement Plan Calculator ===")
    print("Let's calculate your estimated savings at retirement!\n")
    try:
        current_age = int(input("Enter your current age: "))
        retirement_age = int(input("Enter your target retirement age: "))
        
        if current_age >= retirement_age:
            print("Your target retirement age must be greater than your current age!")
            return
            
        current_savings = float(input("Enter your current retirement savings ($): "))
        monthly_contribution = float(input("Enter your planned monthly contribution ($): "))
        annual_return_rate = float(input("Enter your expected annual return rate (e.g. 7 for 7%): "))
        
        total_savings, total_contributions = calculate_retirement(
            current_age, retirement_age, current_savings, monthly_contribution, annual_return_rate
        )
        
        years = retirement_age - current_age
        print("\n" + "="*30)
        print("--- Retirement Projection ---")
        print("="*30)
        print(f"Years to retirement: {years} years")
        print(f"Total contributions (principal): ${total_contributions:,.2f}")
        print(f"Total interest earned: ${(total_savings - total_contributions):,.2f}")
        print(f"Estimated savings at retirement: ${total_savings:,.2f}")
        print("="*30)
        
    except ValueError:
        print("\nInvalid input! Please enter only numerical values.")

if __name__ == "__main__":
    main()
