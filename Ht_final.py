import sys
import HT

if __name__ == "__main__":
    print("Введите, пожалуйста, имя файла, содержащего информацию об электрической цепи (*.xml).")
    f_input_name = sys.argv.pop()
    print("Введите, пожалуйста, имя файла, в который вы желаете записать итоговую таблицу сопротивлений (*.CSV)")
    f_output_name = sys.argv.pop()
    HT.final_answer(f_input_name,f_output_name)
