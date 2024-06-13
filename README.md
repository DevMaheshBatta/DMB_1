# DMB_1
first 
class Solution {
public:
    bool hasCycle(ListNode *head) {
        if( head== NULL)
        return false;

        map<ListNode*,bool>visted;
        ListNode *temp=head;
        while(temp!=NULL)
        {
           if( visted[temp]=true){
            return 1;

           }
           visted[temp]=true;
           temp=temp ->next;


        }
       return false; 
    }
};