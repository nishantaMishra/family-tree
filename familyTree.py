import json
import re

# family data
data = {
    "name": "खदेल मिश्रा", "gender": "male",
    "children": [
        {
            "name": "आयोध्याप्रसाद मिश्रा", "gender": "male",
            "children": [
                {
                    "name": "बेनीमाधव मिश्रा", "gender": "male",
                    "children": [
                        {
                            "name": "राम कृपाल मिश्रा", "gender": "male",
                            "children": [
                                {
                                    "name": "सत्यपाल(कमलेश) मिश्रा", "gender": "male",
                                    "children": [
                                        {
                                            "name": "प्रभात(कन्धैया)", "gender": "male",
                                            "children": [
                                                {"name": "रौनक", "gender": "male"},
                                                {"name": "ऋतिक", "gender": "male"}
                                            ]
                                        },
                                        {
                                            "name": "कृष्ण कुमार(विनीत) मिश्रा", "gender": "male",
                                            "children": [
                                                {"name": "कार्तिक", "gender": "male"}
                                            ]
                                        }
                                    ]
                                },
                                {
                                    "name": "कृष्णपाल(अन्नू) मिश्रा", "gender": "male",
                                    "children": [
                                        {
                                            "name": " अतुल(सोनू)", "gender": "male",
                                            "children": [
                                                {"name": "१", "gender": "male"},
                                                {"name": "२", "gender": "male"}
                                            ]
                                        }
                                    ]
                                },
                                {"name": "बिन्दु(गुलाबकली) मिश्रा", "gender": "female"},
                                {"name": "नानबुदी", "gender": "female"},
                                {"name": "मीनू", "gender": "female"}
                            ]
                        },
                        {
                            "name": "राम शिरोमणि मिश्रा", "gender": "male",
                            "children": [
                                {
                                    "name": "दयाशङ्कर मिश्रा", "gender": "male",
                                    "children": [
                                        {
                                            "name": "उदय शङ्कर मिश्रा", "gender": "male",
                                            "children": [
                                                {"name": "आद्या मिश्रा", "gender": "female"},
                                                {"name": "अभ्युदय मिश्रा", "gender": "male"}
                                            ]
                                        },
                                        {"name": "रविशङ्कर मिश्रा(छोटकौ)", "gender": "male", "details": "विवाह से पूर्व ही इनकी आकाल मृत्यु हो गयी थी।"}
                                    ]
                                },
                                {
                                    "name": "उमाशङ्कर मिश्रा", "gender": "male",
                                    "children": [
                                        {
                                            "name": "अजयशङ्कर(बबलू) मिश्रा", "gender": "male",
                                            "children": [
                                                {"name": "आशी", "gender": "female"},
                                                {"name": "अनन्या", "gender": "female"},
                                                {"name": "नीशू", "gender": "female"},
                                                {"name": "४"}
                                            ]
                                        },
                                        {
                                            "name": "प्रभाशङ्कर(झल्लू) मिश्रा", "gender": "male",
                                            "children": [
                                                {"name": "पारुल", "gender": "female"},
                                                {"name": "२ (पुत्र)", "gender": "male"}
                                            ]
                                        },
                                        {"name": "विजयशङ्कर(फुन्नू) मिश्रा", "gender": "male"}
                                    ]
                                },
                                {"name": "जगिता", "gender": "female", "details": "वुष्णुदत्त तिवारी से विवाहित।", "spouse": {"name": "वुष्णुदत्त तिवारी", "gender": "male"}}
                            ]
                        },
                        {"name": "रमजनिया", "gender": "female", "details": "रामशिरोमणि से आतरसुई में विवाह हुआ।", "spouse": {"name": "रामशिरोमणि", "gender": "male"}},
                        {
                            "name": "सुदामा प्रसाद मिश्रा", "gender": "male",
                            "children": [
                                {
                                    "name": "सुरोश मिश्रा", "gender": "male",
                                    "children": [
                                        {
                                            "name": "प्रमोद मिश्रा (त्यागी)", "gender": "male",
                                            "children": [
                                                {"name": "सानिया", "gender": "female"},
                                                {"name": "अंशिका", "gender": "female"}
                                            ]
                                        },
                                        {
                                            "name": "विनोद मिश्रा (कल्लू)", "gender": "male",
                                            "children": [
                                                {"name": "१(पुत्री)", "gender": "female"},
                                                {"name": "२(पुत्री)", "gender": "female"},
                                                {"name": "३(पुत्र)", "gender": "male"}
                                            ]
                                        },
                                        {
                                            "name": "आनन्द मिश्रा", "gender": "male",
                                            "children": [
                                                {"name": "स्पर्श", "gender": "male"},
                                                {"name": "अविक", "gender": "male"}
                                            ]
                                        }
                                    ]
                                },
                                {
                                    "name": "मुनेश मिश्रा", "gender": "male",
                                    "children": [
                                        {"name": "विकास मिश्रा", "gender": "male"},
                                        {"name": "खुशबू", "gender": "female"},
                                        {"name": "सुभाष मिश्रा", "gender": "male"}
                                    ]
                                },
                                {"name": "सुनीता", "gender": "female"},
                                {"name": "गीता", "gender": "female"},
                                {"name": "सीता", "gender": "female", "details": "इनका निधन आत्मदाह से हुआ था।"},
                                {"name": "ममता", "gender": "female"}
                            ]
                        },
                        {
                            "name": "राम सूरत मिश्रा", "gender": "male", "spouse": {"name": "सोनकली मिश्रा", "gender": "female"},
                            "children": [
                                {
                                    "name": "अनुराधा तिवारी", "gender": "female", "spouse": {"name": "अवधेश प्रताप तिवारी", "gender": "male"},
                                    "children": [
                                        {"name": "प्रभु नारायण तिवारी", "gender": "male", "spouse": {"name": "रश्मि तिवारी", "gender": "female"}},
                                        {"name": "अंशु तिवारी", "gender": "female", "details": "रवि मिश्रा सङ्ग विवाहित", "spouse": {"name": "रवि मिश्रा", "gender": "male"}}
                                    ]
                                },
                                {
                                    "name": "श्रवण कुमार मिश्रा", "gender": "male", "spouse": {"name": "शीला मिश्रा", "gender": "female"},
                                    "children": [
                                        {"name": "चेतना", "gender": "female", "spouse": {"name": "पङ्कज तिवारी", "gender": "male"}},
                                        {"name": "भावना", "gender": "female"},
                                        {"name": "प्रेरणा", "gender": "female", "url": "https://www.instagram.com/mishraprerna269/"},
                                        {"name": "निशान्त मिश्रा", "gender": "male"}
                                    ]
                                },
                                {"name": "आशिष कुमार मिश्रा", "gender": "male", "spouse": {"name": "प्रियाङ्का मिश्रा", "gender": "female"}, "children": [{"name": "इडिका", "gender": "female"}]}
                            ]
                        }
                    ]
                },
                {
                    "name": "राम आश्रय मिश्रा", "gender": "male",
                    "children": [
                        {
                            "name": "राम प्रसाद मिश्रा", "gender": "male",
                            "children": [
                                {
                                    "name": "अशोक कुमार (मुन्नू) मिश्रा", "gender": "male",
                                    "children": [
                                        {"name": "गुलाव (सिण्टू) मिश्रा", "gender": "male"},
                                        {"name": "टिङ्कल", "gender": "female"}
                                    ]
                                },
                                {
                                    "name": "मनोज मिश्रा", "gender": "male",
                                    "children": [
                                        {"name": "१(पुत्री)", "gender": "female"},
                                        {"name": "२(पुत्री)", "gender": "female"},
                                        {"name": "३(पुत्री)", "gender": "female"},
                                        {"name": "दीपू मिश्रा", "gender": "male"}
                                    ]
                                },
                                {
                                    "name": "प्रदीप मिश्रा (छोटकौ)", "gender": "male",
                                    "children": [
                                        {"name": "प्रांशु", "gender": "male"},
                                        {"name": "अंश", "gender": "male"}
                                    ]
                                },
                                {"name": "गुड्डन्", "gender": "male"},
                                {"name": "करुणा", "gender": "female"},
                                {"name": "पुष्पा", "gender": "female"},
                                {"name": "सुधा", "gender": "female"}
                            ]
                        },
                        {"name": "सावित्री", "gender": "female"}
                    ]
                },
                {
                    "name": "नारायण दीन मिश्रा", "gender": "male",
                    "children": [
                        {
                            "name": "सतीश मिश्रा", "gender": "male",
                            "children": [
                                {"name": "नीलू", "gender": "female"},
                                {"name": "रेखा", "gender": "female"},
                                {"name": " माधुरी (गुड्डी)", "gender": "female"}
                            ]
                        },
                        {
                            "name": "केशव", "gender": "male",
                            "children": [
                                {"name": "अजीता (रानी)", "gender": "female"},
                                {"name": "अजय (गुडड्डू)", "gender": "male"},
                                {"name": "अजीत (अज्जू)", "gender": "male"}
                            ]
                        },
                        {
                            "name": "दिवाकर मिश्रा", "gender": "male", "details": "उमादेवी मिश्रा से विवाहित।", "spouse": {"name": "उमादेवी मिश्रा", "gender": "female"},
                            "children": [
                                {
                                    "name": "विजय कुमार(बिज्जू) मिश्रा", "gender": "male", "details": "सरिता मिश्रा से विवाहित।", "spouse": {"name": "सरिता मिश्रा", "gender": "female"},
                                    "children": [
                                        {"name": "शुभम् मिश्रा", "gender": "male", "details": "अन्नपूर्णा तिवारी से विवाहित हुआ। अन्नपूर्णा(प्राची) श्री कमलेश तथा श्रीमति ऊषा तिवारी का पुत्री हैं।", "spouse": {"name": "अन्नपूर्णा तिवारी", "gender": "female"}}
                                    ]
                                },
                                {"name": "२"},
                                {"name": "३"},
                                {"name": "४"},
                                {"name": "५"}
                            ]
                        }
                    ]
                }
            ]
        },
        {"name": "भगवानप्रसाद मिश्रा", "gender": "male", "details": "आकाशीय बिजली की चपेट में आने से इनकी असमय मृत्यु हो गयी थी।"}
    ]
}

data_json = json.dumps(data, ensure_ascii=False)

with open('index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Replace the data in the existing index.html
pattern = r'(var data = ).*?(;)'
replacement = f'var data = {data_json};'

# Using re.sub with a function to avoid escape character issues in replacement string
def replace_func(match):
    return f'var data = {data_json};'

new_html = re.sub(pattern, replace_func, html_content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Data updated successfully in index.html")
