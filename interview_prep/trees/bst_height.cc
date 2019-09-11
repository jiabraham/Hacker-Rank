
/*The tree node has data, left child and right child 
class Node {
    int data;
    Node* left;
    Node* right;
};

*/  
    int doHeight(Node* root, int height) {
        height++;
        if (root->left == NULL && root->right == NULL) {
            return height;
        }
        if (root->left == NULL) {
            return doHeight(root->right, height);
        }
        if (root->right == NULL) {
            return doHeight(root->left, height);
        }
        return max(doHeight(root->left, height), doHeight(root->right, height));
    }
    int height(Node* root) {
        return doHeight(root, -1);
    }

