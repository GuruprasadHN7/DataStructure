public class Stack{

    static int MaxSize=100;
    int top;
    int A[]=new int[MaxSize];

    Stack(){
        top=-1;
    }

    void push(int item){
        if(top>MaxSize-1){
            System.out.println("System overflow");
        }
        else{
            A[++top]=item;
        }
    }

    int pop(){
        int elementdeleted;
        if(top<0){
            System.out.println("System underflow");
            return 0;
        }
        else{
            elementdeleted=A[top--];
            return  elementdeleted;
        }
    }

    void display()
    {
        for(int i=0;i<=top;i++){
            System.out.println(A[i]);
        }
    }


    public static void main(String args[]){
        Stack s =new Stack();
        s.push(4);
        s.push(3);
        s.push(2);
        s.display(); //display the stack elements
        s.pop(); // deleting the last element
        s.display(); // display the remaing element
    }
}