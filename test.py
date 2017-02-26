from module import module
from jinja2 import Template ,Environment, PackageLoader
from v_port import v_port
import sys
sys.path.append('..')
env = Environment(loader=PackageLoader('jay_verilog'))
i_a =  v_port('input', 'a_i', 'reg', 3)
i_b =  v_port('input', 'b_i', 'reg', 1)
i_c =  v_port( 'input','c_i', 'wire', 2, comment = 'just test comments')

o_a = v_port('output', 'a_o', 'reg', 1)
o_b = v_port( 'output','b_o', 'wire', 16, comment = 'just comments')
o_c = v_port('output', 'c_o', 'reg', 1)

fab_in = [i_a, i_b, i_c]
fab_out = [o_a, o_b, o_c]
m_fab = module('fab', fab_in + fab_out)

temp = env.get_template('module.html')

print(temp.render(module = m_fab))
