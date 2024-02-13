import calendar

def solution(month, year):
    # Get the month name and calendar matrix
    month_name = calendar.month_name[month]
    cal = calendar.monthcalendar(year, month)

    # Generate the HTML table
    html_table = f'<table border="0" cellpadding="0" cellspacing="0" class="month"><tr><th colspan="7" class="month">{month_name} {year}</th></tr><tr>'
    for day in calendar.day_abbr:
        html_table += f'<th class="{day.lower()}">{day}</th>'
    html_table += '</tr>'

    for week in cal:
        html_table += '<tr>'
        for i, day in enumerate(week):
            if day == 0:
                html_table += '<td class="noday">&nbsp;</td>'
            else:
                html_table += f'<td class="{calendar.day_abbr[i].lower()}">{day}</td>'
        html_table += '</tr>'
    html_table += '</table>'
    
    return html_table


# Test the function
print(solution(11, 2016))