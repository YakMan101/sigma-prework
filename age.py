from datetime import datetime


def ask_for_age():
    format = '%d-%m-%Y'
    while True:
        date_string = input('Enter Date Time (DD-MM-YYYY): ')
        try:
            date = datetime.strptime(date_string, format)
            return (date)

        except ValueError:
            print('Invalid date input, please try again...')


def calculate_year_delta(start_date, end_date):
    year_delta = end_date.year - start_date.year

    if year_delta == 0:
        return year_delta

    month_day_delta = int(start_date.strftime('%m%d')) - \
        int(end_date.strftime('%m%d'))

    if year_delta > 0 and month_day_delta > 0:
        return year_delta - 1

    elif year_delta < 0 and month_day_delta < 0:
        return year_delta + 1

    return year_delta


def age_calculator():
    start_date = ask_for_age()
    end_date = datetime.now()
    delta = calculate_year_delta(start_date, end_date)

    units = 'Year' if delta**2 == 1 else 'Years'

    if delta >= 0:
        print(f'Age: {delta} {units}')
    else:
        print(f'Age in the future: {-delta} {units}')


if __name__ == '__main__':
    age_calculator()
