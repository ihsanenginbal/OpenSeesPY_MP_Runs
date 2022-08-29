# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 00:18:47 2021

@author: Ihsan Engin Bal
Professor in Earthquake Resistant Structures
Hanze University of Applied Sciences Groningen, Netherlands
i.e.bal@pl.hanze.nl

This function is created to find the normal of the plane tangent to the yield surface. The
yield surface is based on the work by Lu and Heuer (2007) and the original work by
Ganz and Thürlimann (1985).

The functions returns the vector ABG, which contains the alfa, beta and gamma coefficients for this brick element
"""
#def 2D_RC_Beam_T_Section(section_tag, hs, hb, bs, bw, cover, Re, concrete_tags, adet1, adet2, adet3, adet4):
def RC_Beam_T_Section_2D(section_tag, hs, hb, bs, bw, cover, distance, Re, concrete_tags):    
    
    import openseespy.opensees as os
    
    
    adet1=round(cover/distance)
    adet2=round(hs/distance)
    adet3=round(((hs+hb)/2-2*cover)/distance)
    adet4=round((hb-cover)/distance)
    
    os.section('Fiber', section_tag)
    # Create the concrete core fibers
    os.patch('quad',concrete_tags[0],1,adet3,-hb+cover, bw/2-cover, -hb+cover, -bw/2+cover, hs-cover, -bw/2+cover, hs-cover, bw/2-cover)	# Beam Core	
    os.patch('quad',concrete_tags[1],1,adet1,-hb, bw/2,-hb, -bw/2, -hb+cover, -bw/2, -hb+cover, bw/2) 				 # Bottom unconfined layer
    os.patch('quad',concrete_tags[1],1,adet4, -hb+cover, -bw/2+cover, -hb+cover, -bw/2, 0.0, -bw/2, 0.0, -bw/2+cover) 		 # Left unconfined layer
    os.patch('quad',concrete_tags[1],1,adet4, -hb+cover, bw/2, -hb+cover, bw/2-cover, 0.0, bw/2-cover, 0.0, bw/2) 		 # Right unconfined layer
    os.patch('quad',concrete_tags[1],1,adet1, hs-cover, bw/2-cover, hs-cover, -bw/2+cover, hs, -bw/2+cover, hs, bw/2-cover) # Unconfined part above the beam core
    os.patch('quad',concrete_tags[1],1,adet2, 0.0, -bw/2+cover, 0.0, -bs/2, hs, -bs/2, hs, -bw/2+cover)		# left unconfined slab block	  	
    os.patch('quad',concrete_tags[1],1,adet2, 0.0, bs/2, 0.0, bw/2-cover, hs, bw/2-cover, hs, bs/2)		# right unconfined slab block
    
        # Create reinforcement fibers
    if Re[0][0]>0:
        As=3.1415*Re[0][1]*Re[0][1]/4              # reinforcement area
        os.fiber(hs-cover, 0, Re[0][0]*As, Re[0][2])	     # Top beam reinforcement
    if Re[1][0]>0:
        As=3.1415*Re[1][1]*Re[1][1]/4              # reinforcement area
        os.fiber(hs-cover, 0, Re[1][0]*As, Re[1][2])	 # Slab reinforcement	
    if Re[2][0]>0:
        As=3.1415*Re[2][1]*Re[2][1]/4    # reinforcement area
        os.fiber(-hb+(hs+hb)/2, 0, Re[2][0]*As, Re[2][2])	  # Body reinforcement
    if Re[3][0]>0:
        As=3.1415*Re[3][1]*Re[3][1]/4    # reinforcement area
        os.fiber(-hb+cover, 0, Re[3][0]*As, Re[3][2])	  # Bottom reinforcement
        
    return


def RC_Rectangular_Column_Section_2D(section_tag, colDepth, colWidth, cover, distance, Re, concrete_tags):    
    
    import openseespy.opensees as os
    
    H=colDepth/2
    B=colWidth/2
    h=H-cover
    b=B-cover
    
    adet1=round(cover/distance)
    adet2=round(2*h/distance)
    
    os.section('Fiber', section_tag)
    # Create the concrete core fibers
    os.patch('quad',concrete_tags[0],1,adet2,-h,b,-h,-b,h,-b,h,b)	# Core
    os.patch('quad',concrete_tags[1],1,adet1,h,b,h,-b,H,-b,H,b)	    # Top Leaf 
    os.patch('quad',concrete_tags[1],1,adet1,-H,b,-H,-b,-h,-b,-h,b)	# Bottom Leaf
    os.patch('quad',concrete_tags[1],1,adet2,-H,-b,-H,-B,H,-B,H,-b)	# Left Leaf
    os.patch('quad',concrete_tags[1],1,adet2,-H,B,-H,b,H,b,H,B)	    # Right Leaf
    # Create reinforcement fibers
    if Re[0][0]>0:
        As=3.1415*Re[0][1]*Re[0][1]/4              # reinforcement area
        os.fiber(h, 0, Re[0][0]*As, Re[0][2])	     # Top reinforcement
    if Re[1][0]>0:
        As=3.1415*Re[1][1]*Re[1][1]/4              # reinforcement area
        os.fiber(h/3, 0, Re[1][0]*As, Re[1][2])	 # Top-body reinforcement	
    if Re[2][0]>0:
        As=3.1415*Re[2][1]*Re[2][1]/4    # reinforcement area
        os.fiber(0, 0, Re[2][0]*As, Re[2][2])	  # Central-body reinforcement
    if Re[3][0]>0:
        As=3.1415*Re[3][1]*Re[3][1]/4    # reinforcement area
        os.fiber(-h/3, 0, Re[3][0]*As, Re[3][2])	  # Bottom-body reinforcement
    if Re[4][0]>0:
        As=3.1415*Re[4][1]*Re[4][1]/4    # reinforcement area
        os.fiber(-h, 0, Re[4][0]*As, Re[4][2]) 	  # Bottom reinforcement
        
    return