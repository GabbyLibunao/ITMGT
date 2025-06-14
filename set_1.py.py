def savings(gross_pay, tax_rate, expenses):
    x = tax_rate*gross_pay
    final_value = int(gross_pay - x - expenses)
    return final_value