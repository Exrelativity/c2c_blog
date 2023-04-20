from django.forms import ModelForm
from .models import UsersProfile
from file.models import File
from django import forms

# def mediaQueryset(request):
#     try:
#         queryset = File.objects.filter(userId = request.user.id)
#     except File.DoesNotExist:
#         return None
#     return queryset

class UsersProfileForm(ModelForm):
    GENDERSET = (('M', 'Male'),
                 ('F', 'Female'))
    COUNTRY =  (("AF","select country"),
                ("AF","Afghanistan"),
                ("AX","Aland Islands"),
                ("AL","Albania"),
                ("DZ","Algeria"),
                ("AS","American Samoa"),
                ("AD","Andorra"),
                ("AO","Angola"),
                ("AI","Anguilla"),
                ("AQ","Antarctica"),
                ("AG","Antigua and Barbuda"),
                ("AR","Argentina"),
                ("AM","Armenia"),
                ("AW","Aruba"),
                ("AU","Australia"),
                ("AT","Austria"),
                ("AZ","Azerbaijan"),
                ("BS","Bahamas"),
                ("BH","Bahrain"),
                ("BD","Bangladesh"),
                ("BB","Barbados"),
                ("BY","Belarus"),
                ("BE","Belgium"),
                ("BZ","Belize"),
                ("BJ","Benin"),
                ("BM","Bermuda"),
                ("BT","Bhutan"),
                ("BO","Bolivia"),
                ("BQ","Bonaire, Sint Eustatius and Saba"),
                ("BA","Bosnia and Herzegovina"),
                ("BW","Botswana"),
                ("BV","Bouvet Island"),
                ("BR","Brazil"),
                ("IO","British Indian Ocean Territory"),
                ("BN","Brunei Darussalam"),
                ("BG","Bulgaria"),
                ("BF","Burkina Faso"),
                ("BI","Burundi"),
                ("KH","Cambodia"),
                ("CM","Cameroon"),
                ("CA","Canada"),
                ("CV","Cape Verde"),
                ("KY","Cayman Islands"),
                ("CF","Central African Republic"),
                ("TD","Chad"),
                ("CL","Chile"),
                ("CN","China"),
                ("CX","Christmas Island"),
                ("CC","Cocos (Keeling) Islands"),
                ("CO","Colombia"),
                ("KM","Comoros"),
                ("CG","Congo"),
                ("CD","Congo, Democratic Republic of the Congo"),
                ("CK","Cook Islands"),
                ("CR","Costa Rica"),
                ("CI","Cote D'Ivoire"),
                ("HR","Croatia"),
                ("CU","Cuba"),
                ("CW","Curacao"),
                ("CY","Cyprus"),
                ("CZ","Czech Republic"),
                ("DK","Denmark"),
                ("DJ","Djibouti"),
                ("DM","Dominica"),
                ("DO","Dominican Republic"),
                ("EC","Ecuador"),
                ("EG","Egypt"),
                ("SV","El Salvador"),
                ("GQ","Equatorial Guinea"),
                ("ER","Eritrea"),
                ("EE","Estonia"),
                ("ET","Ethiopia"),
                ("FK","Falkland Islands (Malvinas)"),
                ("FO","Faroe Islands"),
                ("FJ","Fiji"),
                ("FI","Finland"),
                ("FR","France"),
                ("GF","French Guiana"),
                ("PF","French Polynesia"),
                ("TF","French Southern Territories"),
                ("GA","Gabon"),
                ("GM","Gambia"),
                ("GE","Georgia"),
                ("DE","Germany"),
                ("GH","Ghana"),
                ("GI","Gibraltar"),
                ("GR","Greece"),
                ("GL","Greenland"),
                ("GD","Grenada"),
                ("GP","Guadeloupe"),
                ("GU","Guam"),
                ("GT","Guatemala"),
                ("GG","Guernsey"),
                ("GN","Guinea"),
                ("GW","Guinea-Bissau"),
                ("GY","Guyana"),
                ("HT","Haiti"),
                ("HM","Heard Island and Mcdonald Islands"),
                ("VA","Holy See (Vatican City State)"),
                ("HN","Honduras"),
                ("HK","Hong Kong"),
                ("HU","Hungary"),
                ("IS","Iceland"),
                ("IN","India"),
                ("ID","Indonesia"),
                ("IR","Iran, Islamic Republic of"),
                ("IQ","Iraq"),
                ("IE","Ireland"),
                ("IM","Isle of Man"),
                ("IL","Israel"),
                ("IT","Italy"),
                ("JM","Jamaica"),
                ("JP","Japan"),
                ("JE","Jersey"),
                ("JO","Jordan"),
                ("KZ","Kazakhstan"),
                ("KE","Kenya"),
                ("KI","Kiribati"),
                ("KP","Korea, Democratic People's Republic of"),
                ("KR","Korea, Republic of"),
                ("XK","Kosovo"),
                ("KW","Kuwait"),
                ("KG","Kyrgyzstan"),
                ("LA","Lao People's Democratic Republic"),
                ("LV","Latvia"),
                ("LB","Lebanon"),
                ("LS","Lesotho"),
                ("LR","Liberia"),
                ("LY","Libyan Arab Jamahiriya"),
                ("LI","Liechtenstein"),
                ("LT","Lithuania"),
                ("LU","Luxembourg"),
                ("MO","Macao"),
                ("MK","Macedonia, the Former Yugoslav Republic of"),
                ("MG","Madagascar"),
                ("MW","Malawi"),
                ("MY","Malaysia"),
                ("MV","Maldives"),
                ("ML","Mali"),
                ("MT","Malta"),
                ("MH","Marshall Islands"),
                ("MQ","Martinique"),
                ("MR","Mauritania"),
                ("MU","Mauritius"),
                ("YT","Mayotte"),
                ("MX","Mexico"),
                ("FM","Micronesia, Federated States of"),
                ("MD","Moldova, Republic of"),
                ("MC","Monaco"),
                ("MN","Mongolia"),
                ("ME","Montenegro"),
                ("MS","Montserrat"),
                ("MA","Morocco"),
                ("MZ","Mozambique"),
                ("MM","Myanmar"),
                ("NA","Namibia"),
                ("NR","Nauru"),
                ("NP","Nepal"),
                ("NL","Netherlands"),
                ("AN","Netherlands Antilles"),
                ("NC","New Caledonia"),
                ("NZ","New Zealand"),
                ("NI","Nicaragua"),
                ("NE","Niger"),
                ("NG","Nigeria"),
                ("NU","Niue"),
                ("NF","Norfolk Island"),
                ("MP","Northern Mariana Islands"),
                ("NO","Norway"),
                ("OM","Oman"),
                ("PK","Pakistan"),
                ("PW","Palau"),
                ("PS","Palestinian Territory, Occupied"),
                ("PA","Panama"),
                ("PG","Papua New Guinea"),
                ("PY","Paraguay"),
                ("PE","Peru"),
                ("PH","Philippines"),
                ("PN","Pitcairn"),
                ("PL","Poland"),
                ("PT","Portugal"),
                ("PR","Puerto Rico"),
                ("QA","Qatar"),
                ("RE","Reunion"),
                ("RO","Romania"),
                ("RU","Russian Federation"),
                ("RW","Rwanda"),
                ("BL","Saint Barthelemy"),
                ("SH","Saint Helena"),
                ("KN","Saint Kitts and Nevis"),
                ("LC","Saint Lucia"),
                ("MF","Saint Martin"),
                ("PM","Saint Pierre and Miquelon"),
                ("VC","Saint Vincent and the Grenadines"),
                ("WS","Samoa"),
                ("SM","San Marino"),
                ("ST","Sao Tome and Principe"),
                ("SA","Saudi Arabia"),
                ("SN","Senegal"),
                ("RS","Serbia"),
                ("CS","Serbia and Montenegro"),
                ("SC","Seychelles"),
                ("SL","Sierra Leone"),
                ("SG","Singapore"),
                ("SX","Sint Maarten"),
                ("SK","Slovakia"),
                ("SI","Slovenia"),
                ("SB","Solomon Islands"),
                ("SO","Somalia"),
                ("ZA","South Africa"),
                ("GS","South Georgia and the South Sandwich Islands"),
                ("SS","South Sudan"),
                ("ES","Spain"),
                ("LK","Sri Lanka"),
                ("SD","Sudan"),
                ("SR","Suriname"),
                ("SJ","Svalbard and Jan Mayen"),
                ("SZ","Swaziland"),
                ("SE","Sweden"),
                ("CH","Switzerland"),
                ("SY","Syrian Arab Republic"),
                ("TW","Taiwan, Province of China"),
                ("TJ","Tajikistan"),
                ("TZ","Tanzania, United Republic of"),
                ("TH","Thailand"),
                ("TL","Timor-Leste"),
                ("TG","Togo"),
                ("TK","Tokelau"),
                ("TO","Tonga"),
                ("TT","Trinidad and Tobago"),
                ("TN","Tunisia"),
                ("TR","Turkey"),
                ("TM","Turkmenistan"),
                ("TC","Turks and Caicos Islands"),
                ("TV","Tuvalu"),
                ("UG","Uganda"),
                ("UA","Ukraine"),
                ("AE","United Arab Emirates"),
                ("GB","United Kingdom"),
                ("US","United States"),
                ("UM","United States Minor Outlying Islands"),
                ("UY","Uruguay"),
                ("UZ","Uzbekistan"),
                ("VU","Vanuatu"),
                ("VE","Venezuela"),
                ("VN","Viet Nam"),
                ("VG","Virgin Islands, British"),
                ("VI","Virgin Islands, U.s."),
                ("WF","Wallis and Futuna"),
                ("EH","Western Sahara"),
                ("YE","Yemen"),
                ("ZM","Zambia"),
                ("ZW","Zimbabwe"))
            
    
    firstName = forms.CharField(  
        widget=forms.TextInput(
            attrs={
                "placeholder":"firstName",
                "class":"form-control",
               }
            ))
    
    lastName = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder":"lastName",
                "class":"form-control",
               }
            ))
    
    
    dateOfBirth = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "placeholder":"Date of birth",
                "class":"form-control",
                "type":"date",
                "value":"2001-01-01"}
            ))
    
    gender = forms.CharField(
        widget=forms.Select(
            attrs={
                "placeholder":"gender",
                "class":"form-control"},
            choices=GENDERSET
            ))

    details = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder":"details",
                "class":"form-control"}
            ))
    
    zipcode = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder":"zipcode",
                "class":"form-control"}
            ))
    
    address = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder":"address",
                "class":"form-control"}
            ))
    
    city = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder":"city",
                "class":"form-control"}
            ))
    
    region = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder":"region",
                "class":"form-control"}
            ))
    
    country = forms.CharField(
        widget=forms.Select(
            choices=COUNTRY,
            attrs={
                "placeholder":"country",
                "class":"form-control"}
            ))
    
    longitude = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder":"longitude",
                "class":"form-control"}
            ))
    
    latitude = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder":"latitude",
                "class":"form-control"}
            ))
    
    popularity = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                "placeholder":"popularity",
                "class":"form-control"}
            ))
    image = forms.ChoiceField(
        widget=forms.Select(
            attrs={
            "placeholder":"profile medias",
            "class":"form-control"}
        )
    )
    
    class Meta:
        model = UsersProfile
        fields = ("firstName", "lastName", "dateOfBirth", "gender", "details", "zipcode", "address", "city", "region", "longitude", "latitude", "popularity", "image")

class UsersProfileMutationForm(ModelForm):
    GENDERSET = (('M', 'Male'),
                 ('F', 'Female'))
    COUNTRY = (("AF","select country"),
                ("AF","Afghanistan"),
                ("AX","Aland Islands"),
                ("AL","Albania"),
                ("DZ","Algeria"),
                ("AS","American Samoa"),
                ("AD","Andorra"),
                ("AO","Angola"),
                ("AI","Anguilla"),
                ("AQ","Antarctica"),
                ("AG","Antigua and Barbuda"),
                ("AR","Argentina"),
                ("AM","Armenia"),
                ("AW","Aruba"),
                ("AU","Australia"),
                ("AT","Austria"),
                ("AZ","Azerbaijan"),
                ("BS","Bahamas"),
                ("BH","Bahrain"),
                ("BD","Bangladesh"),
                ("BB","Barbados"),
                ("BY","Belarus"),
                ("BE","Belgium"),
                ("BZ","Belize"),
                ("BJ","Benin"),
                ("BM","Bermuda"),
                ("BT","Bhutan"),
                ("BO","Bolivia"),
                ("BQ","Bonaire, Sint Eustatius and Saba"),
                ("BA","Bosnia and Herzegovina"),
                ("BW","Botswana"),
                ("BV","Bouvet Island"),
                ("BR","Brazil"),
                ("IO","British Indian Ocean Territory"),
                ("BN","Brunei Darussalam"),
                ("BG","Bulgaria"),
                ("BF","Burkina Faso"),
                ("BI","Burundi"),
                ("KH","Cambodia"),
                ("CM","Cameroon"),
                ("CA","Canada"),
                ("CV","Cape Verde"),
                ("KY","Cayman Islands"),
                ("CF","Central African Republic"),
                ("TD","Chad"),
                ("CL","Chile"),
                ("CN","China"),
                ("CX","Christmas Island"),
                ("CC","Cocos (Keeling) Islands"),
                ("CO","Colombia"),
                ("KM","Comoros"),
                ("CG","Congo"),
                ("CD","Congo, Democratic Republic of the Congo"),
                ("CK","Cook Islands"),
                ("CR","Costa Rica"),
                ("CI","Cote D'Ivoire"),
                ("HR","Croatia"),
                ("CU","Cuba"),
                ("CW","Curacao"),
                ("CY","Cyprus"),
                ("CZ","Czech Republic"),
                ("DK","Denmark"),
                ("DJ","Djibouti"),
                ("DM","Dominica"),
                ("DO","Dominican Republic"),
                ("EC","Ecuador"),
                ("EG","Egypt"),
                ("SV","El Salvador"),
                ("GQ","Equatorial Guinea"),
                ("ER","Eritrea"),
                ("EE","Estonia"),
                ("ET","Ethiopia"),
                ("FK","Falkland Islands (Malvinas)"),
                ("FO","Faroe Islands"),
                ("FJ","Fiji"),
                ("FI","Finland"),
                ("FR","France"),
                ("GF","French Guiana"),
                ("PF","French Polynesia"),
                ("TF","French Southern Territories"),
                ("GA","Gabon"),
                ("GM","Gambia"),
                ("GE","Georgia"),
                ("DE","Germany"),
                ("GH","Ghana"),
                ("GI","Gibraltar"),
                ("GR","Greece"),
                ("GL","Greenland"),
                ("GD","Grenada"),
                ("GP","Guadeloupe"),
                ("GU","Guam"),
                ("GT","Guatemala"),
                ("GG","Guernsey"),
                ("GN","Guinea"),
                ("GW","Guinea-Bissau"),
                ("GY","Guyana"),
                ("HT","Haiti"),
                ("HM","Heard Island and Mcdonald Islands"),
                ("VA","Holy See (Vatican City State)"),
                ("HN","Honduras"),
                ("HK","Hong Kong"),
                ("HU","Hungary"),
                ("IS","Iceland"),
                ("IN","India"),
                ("ID","Indonesia"),
                ("IR","Iran, Islamic Republic of"),
                ("IQ","Iraq"),
                ("IE","Ireland"),
                ("IM","Isle of Man"),
                ("IL","Israel"),
                ("IT","Italy"),
                ("JM","Jamaica"),
                ("JP","Japan"),
                ("JE","Jersey"),
                ("JO","Jordan"),
                ("KZ","Kazakhstan"),
                ("KE","Kenya"),
                ("KI","Kiribati"),
                ("KP","Korea, Democratic People's Republic of"),
                ("KR","Korea, Republic of"),
                ("XK","Kosovo"),
                ("KW","Kuwait"),
                ("KG","Kyrgyzstan"),
                ("LA","Lao People's Democratic Republic"),
                ("LV","Latvia"),
                ("LB","Lebanon"),
                ("LS","Lesotho"),
                ("LR","Liberia"),
                ("LY","Libyan Arab Jamahiriya"),
                ("LI","Liechtenstein"),
                ("LT","Lithuania"),
                ("LU","Luxembourg"),
                ("MO","Macao"),
                ("MK","Macedonia, the Former Yugoslav Republic of"),
                ("MG","Madagascar"),
                ("MW","Malawi"),
                ("MY","Malaysia"),
                ("MV","Maldives"),
                ("ML","Mali"),
                ("MT","Malta"),
                ("MH","Marshall Islands"),
                ("MQ","Martinique"),
                ("MR","Mauritania"),
                ("MU","Mauritius"),
                ("YT","Mayotte"),
                ("MX","Mexico"),
                ("FM","Micronesia, Federated States of"),
                ("MD","Moldova, Republic of"),
                ("MC","Monaco"),
                ("MN","Mongolia"),
                ("ME","Montenegro"),
                ("MS","Montserrat"),
                ("MA","Morocco"),
                ("MZ","Mozambique"),
                ("MM","Myanmar"),
                ("NA","Namibia"),
                ("NR","Nauru"),
                ("NP","Nepal"),
                ("NL","Netherlands"),
                ("AN","Netherlands Antilles"),
                ("NC","New Caledonia"),
                ("NZ","New Zealand"),
                ("NI","Nicaragua"),
                ("NE","Niger"),
                ("NG","Nigeria"),
                ("NU","Niue"),
                ("NF","Norfolk Island"),
                ("MP","Northern Mariana Islands"),
                ("NO","Norway"),
                ("OM","Oman"),
                ("PK","Pakistan"),
                ("PW","Palau"),
                ("PS","Palestinian Territory, Occupied"),
                ("PA","Panama"),
                ("PG","Papua New Guinea"),
                ("PY","Paraguay"),
                ("PE","Peru"),
                ("PH","Philippines"),
                ("PN","Pitcairn"),
                ("PL","Poland"),
                ("PT","Portugal"),
                ("PR","Puerto Rico"),
                ("QA","Qatar"),
                ("RE","Reunion"),
                ("RO","Romania"),
                ("RU","Russian Federation"),
                ("RW","Rwanda"),
                ("BL","Saint Barthelemy"),
                ("SH","Saint Helena"),
                ("KN","Saint Kitts and Nevis"),
                ("LC","Saint Lucia"),
                ("MF","Saint Martin"),
                ("PM","Saint Pierre and Miquelon"),
                ("VC","Saint Vincent and the Grenadines"),
                ("WS","Samoa"),
                ("SM","San Marino"),
                ("ST","Sao Tome and Principe"),
                ("SA","Saudi Arabia"),
                ("SN","Senegal"),
                ("RS","Serbia"),
                ("CS","Serbia and Montenegro"),
                ("SC","Seychelles"),
                ("SL","Sierra Leone"),
                ("SG","Singapore"),
                ("SX","Sint Maarten"),
                ("SK","Slovakia"),
                ("SI","Slovenia"),
                ("SB","Solomon Islands"),
                ("SO","Somalia"),
                ("ZA","South Africa"),
                ("GS","South Georgia and the South Sandwich Islands"),
                ("SS","South Sudan"),
                ("ES","Spain"),
                ("LK","Sri Lanka"),
                ("SD","Sudan"),
                ("SR","Suriname"),
                ("SJ","Svalbard and Jan Mayen"),
                ("SZ","Swaziland"),
                ("SE","Sweden"),
                ("CH","Switzerland"),
                ("SY","Syrian Arab Republic"),
                ("TW","Taiwan, Province of China"),
                ("TJ","Tajikistan"),
                ("TZ","Tanzania, United Republic of"),
                ("TH","Thailand"),
                ("TL","Timor-Leste"),
                ("TG","Togo"),
                ("TK","Tokelau"),
                ("TO","Tonga"),
                ("TT","Trinidad and Tobago"),
                ("TN","Tunisia"),
                ("TR","Turkey"),
                ("TM","Turkmenistan"),
                ("TC","Turks and Caicos Islands"),
                ("TV","Tuvalu"),
                ("UG","Uganda"),
                ("UA","Ukraine"),
                ("AE","United Arab Emirates"),
                ("GB","United Kingdom"),
                ("US","United States"),
                ("UM","United States Minor Outlying Islands"),
                ("UY","Uruguay"),
                ("UZ","Uzbekistan"),
                ("VU","Vanuatu"),
                ("VE","Venezuela"),
                ("VN","Viet Nam"),
                ("VG","Virgin Islands, British"),
                ("VI","Virgin Islands, U.s."),
                ("WF","Wallis and Futuna"),
                ("EH","Western Sahara"),
                ("YE","Yemen"),
                ("ZM","Zambia"),
                ("ZW","Zimbabwe"))

    firstName = forms.CharField(  
        widget=forms.TextInput(
            attrs={
                "placeholder":"firstName",
                "class":"form-control"}
            ))
    
    lastName = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder":"lastName",
                "class":"form-control"}
            ))
    
    
    dateOfBirth = forms.DateTimeField(
        widget=forms.DateInput(
            attrs={
                "placeholder":"date of birth",
                "class":"form-control",
                "type":"date"}
            ))
    
    gender = forms.CharField(
        widget=forms.Select(
            attrs={
                "placeholder":"gender",
                "class":"form-control"},
            choices=GENDERSET
            ))
    
    details = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder":"details",
                "class":"form-control",
                "rows":"10", 
                "cols":"100",
                "placeholder":"Here can be your description, Put relevant infomation, like jobs and what you want others to know about you"}
            ))
    
    zipcode = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder":"zipcode",
                "class":"form-control"}
            ))
    
    address = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder":"address",
                "class":"form-control"}
            ))
    
    city = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder":"city",
                "class":"form-control"}
            ))
    
    region = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder":"region",
                "class":"form-control"}
            ))

    country = forms.CharField(
        widget=forms.Select(
            attrs={
                "placeholder":"country",
                "class":"form-control"},
            choices=COUNTRY,
            ))

    longitude = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder":"longitude",
                "class":"form-control",
                "id":"lng"}
            ))
    
    latitude = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder":"latitude",
                "class":"form-control",
                "id":"lat"}
            ))
    
    popularity = forms.FloatField(
        widget=forms.HiddenInput(
            attrs={
                "placeholder":"popularity",
                "class":"form-control"}
            ))
    
    image = forms.ChoiceField(
        widget=forms.Select(
            attrs={
            "placeholder":"profile medias",
            "class":"form-control"}
        )
    )
    
    class Meta:
        model = UsersProfile
        fields = ("firstName", "lastName", "dateOfBirth", "gender", "details", "zipcode", "address", "city", "region", "longitude", "latitude", "popularity", "image")
