# Evaluate bodmas expression "100+(2+12)/14"

predict_params = ['/', '*', '+', '-']


def calculator(param_list=None):
    while '/' in param_list:
        index_no = param_list.index('/')
        val = param_list[index_no - 1] / param_list[index_no + 1]
        param_list = param_list[0:index_no - 1] + [val] + param_list[index_no + 2:]
    while '*' in param_list:
        index_no = param_list.index('*')
        val = param_list[index_no - 1] * param_list[index_no + 1]
        param_list = param_list[0:index_no - 1] + [val] + param_list[index_no + 2:]
    while '+' in param_list:
        index_no = param_list.index('+')
        val = param_list[index_no - 1] + param_list[index_no + 1]
        param_list = param_list[0:index_no - 1] + [val] + param_list[index_no + 2:]
    while '-' in param_list:
        index_no = param_list.index('-')
        val = param_list[index_no - 1] - param_list[index_no + 1]
        param_list = param_list[0:index_no - 1] + [val] + param_list[index_no + 2:]

    return param_list[0]


def segregate_all_param(data=None):
    param_list = list()
    num, c, d_diviser, decimal_flag = 0, 0, 10, False
    for i, d in enumerate(data):
        try:
            if d == '.':
                decimal_flag = True
                continue
            if decimal_flag:
                num = num + float(d) / d_diviser
                d_diviser *= 10
            else:
                num = num * 10 ** c + float(d)
                c = 1
            if i == len(data) - 1:
                param_list.append(num)
        except Exception as e:
            param_list.append(num)
            num, c, d_diviser, decimal_flag = 0, 0, 10, False
            if d in predict_params:
                param_list.append(d)
            else:
                raise Exception("Please enter valid segment")
    return param_list


def separate_brackets(params=None):
    if '(' and ')' in params:
        open_splitter = params.split('(')
        if len(open_splitter) == 2:
            each_data = open_splitter[1].split(')')[0]
        else:
            for val in open_splitter[1:]:
                if ')' in val:
                    each_data = val.split(')')[0]
        data = calculate_element(each_data)
        params = params.replace('(' + each_data + ')', str(data))
        return params


def calculate_element(elem=None):
    while '(' and ')' in elem:
        elem = separate_brackets(elem)
    ls = segregate_all_param(elem)
    result = calculator(ls)
    return result


def calculate_str(data=None):
    try:
        ans = calculate_element(data)
        print(ans)
    except Exception as e:
        raise Exception("Please provide a valid segment")


calculate_str("100/(10-(3*3))+(2+12)/14")
