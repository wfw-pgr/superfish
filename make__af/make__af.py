import numpy as np


# ========================================================= #
# ===  make__af.py ( for superfish )                    === #
# ========================================================= #

def make__af():

    # ------------------------------------------------- #
    # --- [1] Load parameters                       --- #
    # ------------------------------------------------- #

    import nkUtilities.load__constants as lcn
    cnfFile = "dat/parameter.conf"
    const   = lcn.load__constants( inpFile=cnfFile )
    
    print()
    print( "[make__af]  outFile :: {0}".format( const["outFile"] ) )
    print()

    # ------------------------------------------------- #
    # --- [2] comment & settings part               --- #
    # ------------------------------------------------- #
    
    comment  = \
        "### {0} GHz Cavity\n"\
        "### squared shape cavity with a bore tube\n"\
        "### created by K.Nishida (2020/08)\n"\
        "\n\n".format( const["frequency"] )
    
    settings = \
        "&reg kprob=1,            ! superfish problem\n"\
        "icylin=1,                ! cylindrical geometry\n"\
        "conv={0},                ! univ conversion ( cm => mm )\n"\
        "freq={1},                ! RF Frequency\n"\
        "dx={2},                  ! mesh interval\n"\
        "xdri={3},ydri={4},       ! Drive point of RF\n"\
        "kmethod=1,               ! Use beta to compute wave number\n"\
        "beta={5} &               ! Particle velocity for transit-time integrals\n"\
        "\n\n".format( const["unit_conversion"], const["frequency"]*1000.0, const["delta"], \
                       const["xy_drive"][0]    , const["xy_drive"][1]     , const["beta"] )


    # ------------------------------------------------- #
    # --- [3] coordinate settings                   --- #
    # ------------------------------------------------- #

    b        = const["cell_radius"]
    d        = const["cell_length"]
    a        = const["aperture_radius"]
    t        = const["aperture_length"]
    hd       = const["cell_length"]     * 0.5
    ht       = const["aperture_length"] * 0.5

    pts      = [ [           0.0,    0.0 ],
                 [           0.0,      b ],
                 [         hd-ht,      b ],
                 [         hd-ht,   a+ht ],
                 [         hd+ht,   a+ht ],
                 [         hd+ht,      b ],
                 [     d + hd-ht,      b ],
                 [     d + hd-ht,   a+ht ],
                 [     d + hd+ht,   a+ht ],
                 [     d + hd+ht,      b ],
                 [ 2.0*d + hd-ht,      b ],
                 [ 2.0*d + hd-ht,   a+ht ],
                 [ 2.0*d + hd+ht,   a+ht ],
                 [ 2.0*d + hd+ht,      b ],
                 [ 3.0*d        ,      b ],
                 [ 3.0*d        ,    0.0 ],
                 [           0.0,    0.0 ]
    ]
    pts      = np.array( pts )
    
    x_,y_    = 0, 1
    geometry = ""
    npts     = pts.shape[0]
    for ik in range( npts ):
        geometry += "$po x={0}, y={1} $\n".format( pts[ik,x_], pts[ik,y_] )

    # ------------------------------------------------- #
    # --- [4] write in a file                       --- #
    # ------------------------------------------------- #
        
    with open( const["outFile"], "w" ) as f:
        f.write( comment  )
        f.write( settings )
        f.write( geometry )
        
    return()


# ========================================================= #
# ===   実行部                                          === #
# ========================================================= #

if ( __name__=="__main__" ):
    make__af()
