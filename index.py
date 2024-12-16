import aggregation_1
import aggregation_2
import correlation
import normalization_distribution
import outliering
import define_hypothesis

if __name__ == "__main__":
    choice = 1
    while choice != 8:
        print("\nWelcome to Sahil's Tourism Database")
        print("Our dataset includes data from 2019 to 2022.")
        print("1. Get quarterly visualization of a specific country")
        print("2. Get countries visualization for a specific quarter")
        print("3. Get countries visualization for a specific Type of Tourist")
        print("4. Get montly wise correlation between number of tourist")
        print("5. Get montly normalized distribution analysis")
        print("6. Get montly Outliers as number of tourists")
        print("7. Get the Hypothesis testing analysis")
        print("8. EXIT")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            aggregation_1.visualize_tourism_data_by_country()
        elif choice == 2:
            aggregation_1.visualize_tourism_data_by_quarter()
        elif choice == 3:
            aggregation_2.visualize_tourism_data_by_age_group()
        elif choice == 4:
            correlation.plot_correlation_heatmap()
        elif choice == 5:
            normalization_distribution.normalize_and_analyze_distribution()
        elif choice == 6:
            outliering.outliers_by_month()
        elif choice == 7:
            define_hypothesis.hypoTest()
        elif choice == 8:
            print("Exiting... Goodbye!")
        else:
            print("Invalid choice. Please select 1, 2, or 3.")
