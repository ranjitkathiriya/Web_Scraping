from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
from datetime import datetime

def try_parsing_date(text):
    for fmt in ('%d %b %Y', '%b %d %Y'):
        try:
            return datetime.strptime(text, fmt)
        except ValueError:
            pass
    raise ValueError('no valid date format found')

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

dicts_country = {'Afghanistan': 160, 'Albania': 93, 'Algeria': 123, 'American Samoa': 207, 'Andorra': 97, 'Angola': 127, 'Anguilla': 217, 'Antigua and Barbuda': 221, 'Argentina': 37, 'Armenia': 102, 'Aruba': 177, 'Australia': 29, 'Austria': 36, 'Azerbaijan': 85, 'Bahamas': 110, 'Bahrain': 133, 'Bangladesh': 233, 'Barbados': 112, 'Belarus': 83, 'Belgium': 31, 'Belize': 193, 'Benin': 148, 'Bermuda': 113, 'Bhutan': 198, 'Bolivia, Plurinational State of': 53, 'Bosnia and Herzegovina': 86, 'Botswana': 144, 'Brazil': 33, 'Virgin Islands, British': 224, 'Brunei Darussalam': 79, 'Bulgaria': 73, 'Burkina Faso': 165, 'Burundi': 166, 'Cambodia': 140, 'Cameroon': 134, 'Canada': 27, 'Cabo Verde': 157, 'Cayman Islands': 111, 'Central African Republic': 167, 'Chad': 161, 'Chile': 43, 'China': 41, 'Colombia': 46, 'Comoros': 172, 'Congo': 84, 'Cook Islands': 208, 'Costa Rica': 58, 'Croatia': 28, 'Cuba': 51, 'Curaçao': 189, 'Cyprus': 94, 'Czechia': 3, 'Denmark': 2, 'Djibouti': 153, 'Dominica': 229, 'Dominican Republic': 52, 'Ecuador': 49, 'Egypt': 80, 'El Salvador': 55, 'Equatorial Guinea': 61, 'Eritrea': 168, 'Estonia': 72, 'Ethiopia': 81, 'Falkland Islands (Malvinas)': 219, 'Faroe Islands': 175, 'Fiji': 180, 'Finland': 24, 'France': 5, 'French Guiana': 235, 'French Polynesia': 205, 'Gabon': 150, 'Gambia': 149, 'Georgia': 87, 'Germany': 8, 'Ghana': 118, 'Gibraltar': 119, 'Greece': 11, 'Greenland': 138, 'Gregorian calendar': 22, 'Grenada': 182, 'Guadeloupe': 236, 'Guam': 188, 'Guatemala': 50, 'Guernsey': 191, 'Guinea': 169, 'Guinea-Bissau': 173, 'Guyana': 227, 'Haiti': 103, 'Honduras': 54, 'Hong Kong': 42, 'Hungary': 12, 'Iceland': 88, 'India': 35, 'Indonesia': 65, 'Iran, Islamic Republic of': 75, 'Iraq': 109, 'Ireland': 32, 'Isle of Man': 234, 'Israel': 34, 'Italy': 13, 'Ivory Coast': 125, 'Jamaica': 117, 'Japan': 26, 'Jersey': 192, 'Jordan': 44, 'Julian calendar': 23, 'Kazakhstan': 82, 'Kenya': 105, 'Kiribati': 194, 'Kosovo': 120, 'Kuwait': 108, 'Kyrgyzstan': 136, 'La Réunion': 176, 'Laos': 200, 'Latvia': 89, 'Lebanon': 121, 'Lesotho': 163, 'Liberia': 129, 'Libya': 124, 'Liechtenstein': 96, 'Lithuania': 90, 'Luxembourg': 17, 'Macau': 186, 'North Macedonia': 92, 'Madagascar': 156, 'Malawi': 162, 'Malaysia': 69, 'Maldives': 201, 'Mali': 152, 'Malta': 95, 'Marshall Islands': 213, 'Martinique': 181, 'Mauritania': 210, 'Mauritius': 143, 'Mayotte': 171, 'Mexico': 40, 'Micronesia, Federated States of': 211, 'Moldova, Republic of': 91, 'Monaco': 99, 'Mongolia': 185, 'Montenegro': 101, 'Montserrat': 220, 'Morocco': 106, 'Mozambique': 126, 'Myanmar': 190, 'Namibia': 130, 'Nauru': 215, 'Nepal': 187, 'New Caledonia': 204, 'New Zealand': 30, 'Nicaragua': 57, 'Niger': 158, 'Nigeria': 77, 'Korea, Democratic Peoples Republic of': 183, 'Northern Mariana Islands': 225, 'Norway': 18, 'Oman': 135, 'Pakistan': 64, 'Palau': 212, 'Panama': 60, 'Papua New Guinea': 202, 'Paraguay': 56, 'Peru': 47, 'Philippines': 67, 'Poland': 14, 'Portugal': 15, 'Puerto Rico': 114, 'Qatar': 107, 'Congo, The Democratic Republic of the': 151, 'Romania': 19, 'Russian Federation': 20, 'Rwanda': 128, 'Saint Barthélemy': 232, 'Saint Helena, Ascension and Tristan da Cunha': 170, 'Saint Kitts and Nevis': 226, 'Saint Lucia': 218, 'Saint Martin (French part)': 231, 'Saint Pierre and Miquelon': 228, 'Saint Vincent and the Grenadines': 222, 'Samoa': 206, 'San Marino': 98, 'Saudi Arabia': 74, 'Senegal': 147, 'Serbia': 38, 'Seychelles': 154, 'Sierra Leone': 164, 'Singapore': 63, 'Sint Maarten (Dutch part)': 230, 'Slovakia': 39, 'Slovenia': 45, 'Solomon Islands': 209, 'Somalia': 137, 'South Africa': 62, 'Korea, Republic of': 70, 'South Sudan': 146, 'Spain': 16, 'Sri Lanka': 116, 'Sudan': 145, 'Suriname': 178, 'Eswatini': 155, 'Sweden': 21, 'Switzerland': 10, 'Syrian Arab Republic': 132, 'São Tomé and Príncipe': 174, 'Taiwan, Province of China': 71, 'Tajikistan': 197, 'Tanzania, United Republic of': 115, 'Thailand': 68, 'Netherlands': 25, 'Timor-Leste': 199, 'Togo': 159, 'Tonga': 195, 'Trinidad and Tobago': 104, 'Tunisia': 122, 'Turkey': 4, 'Turkmenistan': 196, 'Turks and Caicos Islands': 223, 'Tuvalu': 214, 'Virgin Islands, U.S.': 179, 'Uganda': 139, 'Ukraine': 76, 'United Arab Emirates': 66, 'United Kingdom': 9, 'United States': 1, 'Uruguay': 59, 'Uzbekistan': 184, 'Vanuatu': 203, 'Holy See (Vatican City State)': 100, 'Venezuela, Bolivarian Republic of': 48, 'Viet Nam': 78, 'Wallis and Futuna': 216, 'Yemen': 131, 'Zambia': 142, 'Zimbabwe': 141}


country_holiday_list_willdates = []
for country in dicts_country.keys():
    code, name = dicts_country.get(country)
    print(code + ", " + name, country)

    country_holiday_date = []
    name_holiday_dates =[]
    fill_final_dict = {}

    for year in  range(1950,2050):
        print("Year:",year)
        url = "https://www.timeanddate.com/calendar/custom.html?year="+str(year)+"&country="+str(country)+"&cols=1&df=1&lang=en&hol=1"
        html = urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, "html.parser")
        htmltable = soup.find('table', { 'class' : 'cht lpad' })

        if htmltable == None:
            year = int(year) + 1
        else:
            trs = htmltable.find_all('tr')
            year_holiday = []
            name_holiday = []
            # print(len(trs))
            for i in trs:
                # print(i.text)
                # print(i.text[0:5],i.text[5:])
                # print(i.find_all("td")[1].text,i.find("td").text)

                if i.find("td").text is not None:
                    datetimeobject = try_parsing_date(i.find("td").text+" "+str(year)).date()
                    # print(i.find("td").text)

                    year_holiday.append(str(datetimeobject))
                    name_holiday.append(i.find_all("td")[1].text)


            country_holiday_date = country_holiday_date + year_holiday
            name_holiday_dates = name_holiday_dates + name_holiday

    fill_final_dict['country_code'] = code
    fill_final_dict['country_name'] = name
    fill_final_dict['country_holiday_dates'] = country_holiday_date
    fill_final_dict['holiday_name'] = name_holiday_dates

    country_holiday_list_willdates.append(fill_final_dict)
    print(country_holiday_list_willdates)

# jsonData = json.dumps(country_holiday_list_willdates)
# print(jsonData)

# with open('data.json', 'wb') as f:
#     json.dump(jsonData, codecs.getwriter('utf-8')(f), ensure_ascii=False)

# with open('data.json') as data_file:
#     data_loaded = json.load(data_file)
#
# print("Final :",data_loaded)