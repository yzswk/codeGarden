//
//   This file contains the C++ code from Program 5.18 of
//   "Data Structures and Algorithms
//    with Object-Oriented Design Patterns in C++"
//   by Bruno R. Preiss.
//
//   Copyright (c) 1998 by Bruno R. Preiss, P.Eng.  All rights reserved.
//
//   http://www.pads.uwaterloo.ca/Bruno.Preiss/books/opus4/programs/pgm05_18.cpp
//
#ifndef _ASSOCIATION_H_
#define _ASSOCIATION_H_

#include <Object.h>
#include <Ownership.h>


class Association : public Object, public Ownership
{
protected:
    Object* key;
    Object* value;

    int CompareTo (Object const&) const;
public:
    Association (Object&);
    Association (Object&, Object&);
    ~Association ();

    Object& Key () const;
    Object& Value () const;
    
    bool IsNull(void)const 
    {
    	return key->IsNull();
    }
    

    HashValue Hash () const;
    void Put (std::ostream&) const;
};

#endif
