import { Alert, Modal, StyleSheet, Text, View } from "react-native"

const ModalStyled = ({ isVisible, children }) => {
    return (
        <View>
            <Modal
                animationType="slide"
                transparent={true}
                visible={isVisible}
            >
                <View style={styles.centeredView}>
                    <View style={styles.modalView}>
                        {children}
                    </View>
                </View>
            </Modal>
        </View>
    )
}

export default ModalStyled

const styles = StyleSheet.create({
    centeredView: {
      flex: 1,
      justifyContent: "center",
      alignItems: "center",
      marginTop: 22
    },
    modalView: {
      margin: 20,
      backgroundColor: "white",
      borderRadius: 20,
      padding: 35,
      alignItems: "center",
      shadowColor: "#000",
      shadowOffset: {
        width: 0,
        height: 2
      },
      shadowOpacity: 0.25,
      shadowRadius: 4,
      elevation: 5
    },
    modalText: {
      marginBottom: 15,
      textAlign: "center"
    }
  });