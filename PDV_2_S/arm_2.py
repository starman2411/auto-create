import ezdxf as dxf
from point import *


def main(width, heigh, quantity, path=str()):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2)
    msp = doc.modelspace()
    p = point()
    p.msp = msp

    p.go_line(120, 0)
    p.go_arc(8, 10)
    p.go_arc(7, 10)
    p.go_line(0, -2)
    p.go_arc(6, 10)
    p.go_arc(5, 10)
    p.go_line(-120, 0)
    p.go_arc(4, 10)
    p.go_arc(3, 10)
    p.go_line(0, 2)
    p.go_arc(2, 10)
    p.go_arc(1, 10)
    p.go_init()

    p.circle(-2, -11, 2.6)
    p.circle(124, 0, 2.6)

    doc.saveas(path+"Рычаг 2 "+str(width)+'x'+str(heigh) +
               ' 2мм ' + str(quantity * 2)+'шт.dxf')
