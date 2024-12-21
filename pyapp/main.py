from ansi.colour import fg, bg
import aws_cdk.aws_ec2 as ec2

def main():
    print(bg.red(fg.yellow('Hello world!')))

if __name__ == "__main__":
    main()
