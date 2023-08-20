batchlabel = """
^XA

^PON

^FO280,10
^BQN,2,6,H
^FDMM,A{batch}^FS

^CF0,20
^FO20,20^FDBatch^FS
^CF0,70
^FO20,45^FD{batch}^FS

^CF0,20
^FO20,115^FDItem Code^FS
^CF0,40
^FO20,140^FD{item_code}^FS

^CF0,20
^FO20,190^FDDescription^FS
^CF0,20
^FO20,215^FD{description_line1}^FS
^FO20,235^FD{description_line2}^FS

^CF0,20
^FO280,180^FDIncoming^FS
^CF0,40
^FO280,205^FD{warehouse}^FS
^CF0,30
^FO280,245^FD{warehouse_parent}^FS

^CF0,37
^FO280,295^GB132,55,2,B,0^FS
^FO290,310^FD{tower}^FS

^CF0,50
^FO20,275^GB168,75,8,B,0^FS
^FO40,295^FD{msl}^FS

^CF0,20
^FO20,370^FDQty^FS
^CF0,20
^FO20,395^FD{qty}^FS

^CF0,20
^FO90,370^FDDate^FS
^CF0,20
^FO90,395^FD{date}^FS

^CF0,20
^FO210,370^FDUser^FS
^CF0,20
^FO210,395^FD{user}^FS

^XZ
"""

boxlabel = """
^XA

^FWR

^FO610,50
^BQN,2,6,H
^FDMM,AKIT186 - ESODE^FS

^CF0,155
^FO580,250^FDKIT186^FS

^FO500,900^GC250,5,B^FS

^CF0,155
^FO530,940^FDDE^FS

^CFQ,0
^FO540,60^FDWork Order^FS
^CFV,0
^FO460,60^FDWO-DE-23-0142-ST^FS

^CFQ,0
^FO410,860^FDPriority^FS
^CFV,0
^FO330,860^FDStandard^FS

^CFQ,0
^FO410,60^FDItem^FS
^CFV,0
^FO330,60^FDIDO-0001E-01A-DE-ST^FS

^CFQ,0
^FO280,60^FDDescription^FS
^CFV,0
^FO200,60^FDIdoru Pedal v5.0^FS


^CFQ,0
^FO110,60^FDQuantity^FS
^CFU,0
^FO50,60^FD100^FS

^CFQ,0
^FO110,300^FDSales Order^FS
^CFU,0
^FO50,300^FDSO-DE-23-00526^FS

^CFQ,0
^FO110,860^FDType^FS
^CFU,00
^FO50,860^FDFirst Order^FS

^XZ
"""