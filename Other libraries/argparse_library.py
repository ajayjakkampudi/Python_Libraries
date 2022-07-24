# Don't name the file as argparse(it shows error)
import argparse
parser=argparse.ArgumentParser(description="Area of Triangle")
parser.add_argument('-b','--base',type=int,help="Base length",required=True,metavar='')
parser.add_argument('-l','--height',type=int,help="Height length",required=True,metavar='')
args=parser.parse_args()
def areas(base,height):
    area=base*height/2
    return area


if __name__=="__main__":
    print(areas(args.base,args.height))