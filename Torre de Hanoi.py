#TORRE DE HANOI - Felipe Miranda

from FreeCAD import Part
from FreeCAD import Base

#a base da torre
base = Part.makeBox(380, 150,20)

#os cilindros onde de encaixam os discos
cilindro1 = Part.makeCylinder(10,150)
cilindro1.translate(Base.Vector(70, 75))

cilindro2 = Part.makeCylinder(10,150)
cilindro2.translate(Base.Vector(190, 75))

cilindro3 = Part.makeCylinder(10,150)
cilindro3.translate(Base.Vector(310, 75))

#modelos dos discos para furá-lo
modeldisco1 = Part.makeCylinder(50, 20)
furo1 = Part.makeCylinder(10, 20)

modeldisco2 = Part.makeCylinder(45, 20)
furo2 = Part.makeCylinder(10, 20)

modeldisco3 = Part.makeCylinder(40, 20)
furo3 = Part.makeCylinder(10, 20)

modeldisco4 = Part.makeCylinder(35, 20)
furo4 = Part.makeCylinder(10, 20)

modeldisco5 = Part.makeCylinder(30, 20)
furo5 = Part.makeCylinder(10, 20)

modeldisco6 = Part.makeCylinder(25, 20)
furo6 = Part.makeCylinder(10, 20)

#discos que encaixam na torre
disco1 = modeldisco1.cut(furo1)
disco1.translate(Base.Vector(70,75,20))

disco2 = modeldisco2.cut(furo2)
disco2.translate(Base.Vector(190,75,20))

disco3 = modeldisco3.cut(furo3)
disco3.translate(Base.Vector(310,75,20))

disco4 = modeldisco4.cut(furo4)
disco4.translate(Base.Vector(310,75,40))

disco5 = modeldisco5.cut(furo5)
disco5.translate(Base.Vector(190,75,40))

disco6 = modeldisco6.cut(furo6)
disco6.translate(Base.Vector(70,75,40))

#Mostrando os objetos
Part.show(base)
Part.show(cilindro1)
Part.show(cilindro2)
Part.show(cilindro3)
Part.show(disco1)
Part.show(disco2)
Part.show(disco3)
Part.show(disco4)
Part.show(disco5)
Part.show(disco6)

#Criação do documento
doc = FreeCAD.newDocument('Torre de Hanoi')
docBase = doc.addObject("Part::Feature", 'Base')
docBase.Shape = base
docCil1 = doc.addObject("Part::Feature", 'Cilindro 1')
docCil1.Shape = cilindro1
docCil2 = doc.addObject("Part::Feature", 'Cilindro 2')
docCil2.Shape = cilindro2
docCil3 = doc.addObject("Part::Feature", 'Cilindro 3')
docCil3.Shape = cilindro3
docDisco1 = doc.addObject("Part::Feature", 'Disco 1')
docDisco1.Shape = disco1
docDisco2 = doc.addObject("Part::Feature", 'Disco 2')
docDisco2.Shape = disco2
docDisco3 = doc.addObject("Part::Feature", 'Disco 3')
docDisco3.Shape = disco3
docDisco4 = doc.addObject("Part::Feature", 'Disco 4')
docDisco4.Shape = disco4
docDisco5 = doc.addObject("Part::Feature", 'Disco 5')
docDisco5.Shape = disco5
docDisco6 = doc.addObject("Part::Feature", 'Disco 6')
docDisco6.Shape = disco6

#Criação dos grupos
grupo = doc.addObject('App::DocumentObjectGroup', 'Torre_base')
grupo.addObject(docBase)
grupo.addObject(docCil1)
grupo.addObject(docCil2)
grupo.addObject(docCil3)

grupo2 = doc.addObject('App::DocumentObjectGroup', 'Discos')
grupo2.addObject(docDisco1)
grupo2.addObject(docDisco2)
grupo2.addObject(docDisco3)
grupo2.addObject(docDisco4)
grupo2.addObject(docDisco5)
grupo2.addObject(docDisco6)
